from typing import List, Tuple, Dict, Optional
import google.generativeai as genai
import orgparse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from analyzer.models.category import CategoryEnum
from analyzer.utils.embedding import get_embedding


def extract_description(body: str) -> str:
    """
    Extract the description from the body of an Org mode node.

    Args:
        body (str): The body text of an Org mode node.

    Returns:
        str: The extracted description, or an empty string if not found.
    """
    lines = body.strip().splitlines()
    for line in lines:
        if line.startswith("#+begin_src txt :tangle"):
            continue
        if line.startswith("#+end_src"):
            break
        return line.strip()
    return ""


def categorize_description(
    model: genai.GenerativeModel, 
    description: str, 
    priority_categories: List[str]
) -> str:
    """
    Categorize a project description using a generative AI model.

    Args:
        model (genai.GenerativeModel): The generative AI model to use for categorization.
        description (str): The project description to categorize.
        priority_categories (List[str]): A list of category names to prioritize.

    Returns:
        str: The name of the assigned category.
    """
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


def check_similarity(
    papers: List[Dict[str, str]], 
    existing_projects: List[Dict[str, str]]
) -> List[Tuple[Dict[str, str], Dict[str, str], float]]:
    """
    Check similarity between new papers and existing projects.

    Args:
        papers (List[Dict[str, str]]): A list of dictionaries containing paper information.
        existing_projects (List[Dict[str, str]]): A list of dictionaries containing existing project information.

    Returns:
        List[Tuple[Dict[str, str], Dict[str, str], float]]: A list of tuples containing similar paper-project pairs and their similarity score.
    """
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


def merge_projects(target_node: orgparse.OrgNode, source_node: orgparse.OrgNode) -> None:
    """
    Merge two Org mode nodes, combining their descriptions and properties.

    Args:
        target_node (orgparse.OrgNode): The target node to merge into.
        source_node (orgparse.OrgNode): The source node to merge from.
    """
    target_description = extract_description(target_node.get_body())
    source_description = extract_description(source_node.get_body())
    combined_description = f"{target_description}\n\nMerged with {source_node.heading}:\n{source_description}"

    target_node.content = target_node.content.replace(target_description, combined_description)

    for key, value in source_node.properties.items():
        if key not in target_node.properties:
            target_node.properties[key] = value
        elif key == "CATEGORY":
            target_node.properties[key] = f"{target_node.properties[key]}, {value}"

    target_node.properties["MERGED"] = "True"

    target_node._refresh_entries()


def deduplicate_projects(
    filename: str = "PROJECTS.org", 
    similarity_threshold: float = 0.9, 
    interactive: bool = False
) -> List[Tuple[Dict[str, str], Dict[str, str], float]]:
    """
    Deduplicate projects in an Org mode file based on similarity.

    Args:
        filename (str): The name of the Org mode file containing projects.
        similarity_threshold (float): The threshold above which projects are considered similar.
        interactive (bool): Whether to prompt for user input during deduplication.

    Returns:
        List[Tuple[Dict[str, str], Dict[str, str], float]]: A list of similar project pairs and their similarity scores.
    """
    tree = orgparse.load(filename)
    projects = []
    for node in tree[1:]:
        if node.heading:
            description = extract_description(node.get_body())
            projects.append(
                {
                    "name": node.heading,
                    "description": description,
                    "node": node,
                    "embedding": get_embedding(description),
                }
            )

    similar_project_pairs = []
    merged_projects = set()

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
                    "Enter 'm' to merge, 'k' to keep both, or 's' to skip (default is merge): "
                ).lower()
                if action == "":
                    action = "m"  # Default to merging if user just presses Enter
            else:
                action = "m"  # Default to merging in non-interactive mode

            if action == "m":
                if (
                    proj1["name"] not in merged_projects
                    and proj2["name"] not in merged_projects
                ):
                    merge_projects(proj1["node"], proj2["node"])
                    merged_projects.add(proj2["name"])
                    print(f"Merged '{proj2['name']}' into '{proj1['name']}'")
                else:
                    print(
                        f"Skipping merge as one of the projects has already been merged"
                    )
            elif action == "k":
                print("Keeping both projects.")
            else:
                print("Skipping this pair.")
    else:
        print("No similar projects found.")

    if merged_projects:
        new_tree = orgparse.loads(tree.root.to_string())
        new_tree.children = [
            node for node in new_tree.children if node.heading not in merged_projects
        ]

        with open(filename, "w") as f:
            f.write(new_tree.to_string())
        print(f"Updated {filename} with merged projects.")
    else:
        print(f"No changes made to {filename}.")

    return similar_project_pairs
