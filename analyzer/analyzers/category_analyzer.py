import os
import socket
from collections import Counter
from datetime import datetime

import google.generativeai as genai
import orgparse

from analyzer.models.category import CategoryEnum, update_category_enum
from analyzer.utils.embedding import get_embedding
from analyzer.utils.text_processing import categorize_description, extract_description


def get_category_usage(filename="PROJECTS.org"):
    tree = orgparse.load(filename)
    category_usage = Counter()
    total_projects = 0
    for node in tree[1:]:
        if node.heading:
            total_projects += 1
            category = node.get_property("CATEGORY", "")
            if category in CategoryEnum.__members__:
                category_usage[category] += 1
    avg_usage = total_projects / len(CategoryEnum.__members__)
    return category_usage, avg_usage


def categorize_projects(max_refresh=3, max_unknown=5, filename="PROJECTS.org"):
    refresh_count = 0
    while refresh_count < max_refresh:
        tree = orgparse.load(filename)
        is_dirty = False
        unknown_count = 0
        uncategorized_projects = []
        print(f"Categorization attempt {refresh_count + 1} of {max_refresh}")
        model = genai.GenerativeModel("gemini-pro")
        category_usage, avg_usage = get_category_usage(filename)
        over_threshold = avg_usage * 1.5
        under_threshold = avg_usage * 0.5
        over_utilized = [
            c for c, count in category_usage.items() if count > over_threshold
        ]
        under_utilized = [
            c for c, count in category_usage.items() if count < under_threshold
        ]

        for node in tree[1:]:
            if node.heading:
                category = node.get_property("CATEGORY", "")
                description = extract_description(node.body)
                should_recategorize = (
                    not category
                    or category not in CategoryEnum.__members__
                    or category == "UNKNOWN"
                    or category in over_utilized
                    and under_utilized
                )
                if should_recategorize:
                    if unknown_count < max_unknown:
                        print(f"\nCategorizing project: {node.heading}")
                        try:
                            category_new = categorize_description(
                                model, description, under_utilized
                            )
                            if category_new != category:
                                print(
                                    f"Updating category from {category} to {category_new}"
                                )
                                node.properties["CATEGORY"] = category_new
                                node.properties["UPDATED_BY"] = (
                                    f"{os.environ.get('USER')}@{socket.gethostname()}"
                                )
                                node.properties["UPDATED"] = datetime.now().strftime(
                                    "%Y-%m-%d %H:%M:%S"
                                )
                                is_dirty = True
                            else:
                                print(f"Category remains unchanged: {category}")
                                uncategorized_projects.append(
                                    {"name": node.heading, "description": description}
                                )
                        except Exception as e:
                            print(f"Error: {e}")
                            uncategorized_projects.append(
                                {"name": node.heading, "description": description}
                            )
                        unknown_count += 1
                    else:
                        print(
                            f"Skipping categorization for {node.heading} (max unknown limit reached)"
                        )
                        uncategorized_projects.append(
                            {"name": node.heading, "description": description}
                        )
                else:
                    print(
                        f"Skipping categorization for {node.heading} (already categorized as {category})"
                    )

        changes_made = update_readme(tree, is_dirty, filename)

        if uncategorized_projects:
            new_categories = suggest_new_categories(model, uncategorized_projects)
            if new_categories:
                print(f"Suggested new categories: {new_categories}")
                update_category_enum(new_categories)
                print("CategoryEnum updated. Rerunning categorization.")
                refresh_count += 1
                continue

        if changes_made:
            print(f"Changes made. Processed {unknown_count} unknown categories.")
            refresh_count += 1
        else:
            print("No changes made.")
            break

        if unknown_count < max_unknown:
            print("All unknown categories processed. Stopping categorization.")
            break

    if refresh_count == max_refresh:
        print(
            f"Reached maximum number of category refreshes ({max_refresh}). Stopping categorization."
        )


def suggest_new_categories(model, uncategorized_projects):
    prompt = f"Based on these uncategorized projects: {uncategorized_projects}, suggest up to 3 new categories. Return the suggestions as a Python list of uppercase strings with underscores as a delimiter."
    response = model.generate_content(prompt)
    try:
        return ast.literal_eval(response.text)
    except:
        print("Error parsing AI response for new categories. Using empty list.")
        return []


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


def update_readme(tree, is_dirty, filename="PROJECTS.org"):
    if is_dirty:
        # Implementation for updating the README file
        pass
    else:
        print(f"No changes made to {filename}.")
    return is_dirty
