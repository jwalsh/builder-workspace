import orgparse
from analyzer.utils.embedding import get_embedding
from sklearn.metrics.pairwise import cosine_similarity
import google.generativeai as genai
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from analyzer.models.category import CategoryEnum


def extract_description(body):
    lines = body.strip().splitlines()
    for line in lines:
        if line.startswith("#+begin_src txt :tangle"):
            continue
        if line.startswith("#+end_src"):
            break
        return line.strip()
    return ""


def categorize_description(model, description, priority_categories):
    categories = [
        category.name for category in CategoryEnum if category != CategoryEnum.UNKNOWN
    ]
    priority_categories_str = (
        ", ".join(priority_categories) if priority_categories else "None"
    )
    prompt = f"""Which category does this project description belong to? Choose one from the following options: {', '.join(categories)}. 
    Prioritize these under-utilized categories if appropriate: {priority_categories_str}
    Description: {description}"""
    response = model.generate_content(prompt)
    category_name = response.text.strip().upper()
    return (
        category_name
        if category_name in CategoryEnum.__members__
        else CategoryEnum.UNKNOWN.name
    )


def check_similarity(papers, existing_projects):
    all_texts = [(p["title"] + " " + p["abstract"]) for p in papers] + [
        (p["title"] + " " + p.get("description", "")) for p in existing_projects
    ]
    vectorizer = TfidfVectorizer().fit_transform(all_texts)
    cosine_similarities = cosine_similarity(vectorizer)
    similar_projects = []
    for i, paper in enumerate(papers):
        paper_similarities = cosine_similarities[i, len(papers) :]
        most_similar_idx = paper_similarities.argmax()
        if paper_similarities[most_similar_idx] > 0.3:
            similar_projects.append(
                (
                    paper,
                    existing_projects[most_similar_idx],
                    paper_similarities[most_similar_idx],
                )
            )
    return similar_projects


def deduplicate_projects(
    filename="PROJECTS.org", similarity_threshold=0.9, interactive=False
):
    tree = orgparse.load(filename)
    projects = []
    for node in tree[1:]:
        if node.heading:
            description = extract_description(node.body)
            projects.append(
                {
                    "name": node.heading,
                    "description": description,
                    "node": node,
                    "embedding": get_embedding(description),
                }
            )

    similar_project_pairs = []

    for i, project in enumerate(projects):
        for j, other_project in enumerate(projects[i + 1 :]):
            similarity = cosine_similarity(
                [project["embedding"]], [other_project["embedding"]]
            )[0][0]
            if similarity > similarity_threshold:
                similar_project_pairs.append((project, other_project, similarity))

    if similar_project_pairs:
        print(f"Found {len(similar_project_pairs)} similar project pairs:")
        for proj1, proj2, similarity in similar_project_pairs:
            print(
                f"\n- '{proj1['name']}' and '{proj2['name']}' (Similarity: {similarity:.2f})"
            )
            print(f"  Description 1: {proj1['description'][:100]}...")
            print(f"  Description 2: {proj2['description'][:100]}...")

            if interactive:
                action = input(
                    "Enter 'm' to merge, 'k' to keep both, or 's' to skip: "
                ).lower()
                if action == "m":
                    # Implement merging logic here
                    print("Merging projects...")
                elif action == "k":
                    print("Keeping both projects.")
                else:
                    print("Skipping this pair.")
            else:
                print(
                    "Recommendation: Review these projects for potential merging or differentiation."
                )
    else:
        print("No similar projects found.")

    return similar_project_pairs
