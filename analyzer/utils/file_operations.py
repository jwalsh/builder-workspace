import csv
import numpy as np
import orgparse
from analyzer.utils.text_processing import extract_description


def export_projects_to_csv(output_file, filename="PROJECTS.org"):
    tree = orgparse.load(filename)
    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Category", "Project Name", "Description"])
        for node in tree[1:]:
            if node.heading:
                category = node.get_property("CATEGORY", "UNKNOWN")
                description = extract_description(node.body)
                writer.writerow([category, node.heading, description])
    print(f"Projects exported to {output_file}")


def split_data_for_training(input_file, train_file, test_file, test_split=0.2):
    with open(input_file, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)
        data = list(reader)

    np.random.shuffle(data)
    split_index = int(len(data) * (1 - test_split))
    train_data = data[:split_index]
    test_data = data[split_index:]

    with open(train_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(train_data)

    with open(test_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(test_data)

    print(f"Data split into {train_file} and {test_file}")


def load_existing_projects(filename="PROJECTS.org"):
    tree = orgparse.load(filename)
    projects = []
    for node in tree[1:]:
        if node.heading:
            projects.append(
                {
                    "title": node.heading,
                    "description": extract_description(node.body),
                    "category": node.get_property("CATEGORY", ""),
                }
            )
    return projects
