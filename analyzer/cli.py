import click

from analyzer.analyzers.arxiv_analyzer import check_arxiv_papers
from analyzer.analyzers.category_analyzer import categorize_projects
from analyzer.analyzers.similarity_analyzer import (
    analyze_category_similarity,
    analyze_project_similarity,
)
from analyzer.models.category import show_categories
from analyzer.utils.file_operations import (
    export_projects_to_csv,
    split_data_for_training,
)
from analyzer.utils.text_processing import deduplicate_projects


@click.command()
@click.option(
    "--action",
    type=click.Choice(
        [
            "categorize",
            "analyze",
            "categories",
            "export",
            "train-test",
            "deduplicate",
            "check-arxiv",
        ]
    ),
    default="categorize",
    help="Action to perform",
)
@click.option(
    "--max-refresh",
    type=int,
    default=3,
    help="Maximum number of times to refresh categories and re-run categorization.",
)
@click.option(
    "--max-unknown",
    type=int,
    default=5,
    help="Maximum number of unknown categories to process during categorization.",
)
@click.option(
    "--output-file",
    type=str,
    default="projects_for_training.csv",
    help="Output file name for CSV export.",
)
@click.option(
    "--train-file",
    type=str,
    default="train_data.csv",
    help="Output file name for training data.",
)
@click.option(
    "--test-file",
    type=str,
    default="test_data.csv",
    help="Output file name for test data.",
)
@click.option(
    "--test-split",
    type=float,
    default=0.2,
    help="Proportion of data to use for testing (0.0 to 1.0).",
)
@click.option(
    "--filename", type=str, default="PROJECTS.org", help="Input org file name."
)
def main(
    action,
    max_refresh,
    max_unknown,
    output_file,
    train_file,
    test_file,
    test_split,
    filename,
):
    if action == "categorize":
        categorize_projects(max_refresh, max_unknown, filename)
    elif action == "analyze":
        analyze_project_similarity(filename)
        analyze_category_similarity()
    elif action == "categories":
        show_categories()
    elif action == "export":
        export_projects_to_csv(output_file, filename)
    elif action == "train-test":
        export_projects_to_csv(output_file, filename)
        split_data_for_training(output_file, train_file, test_file, test_split)
    elif action == "deduplicate":
        deduplicate_projects(filename)
    elif action == "check-arxiv":
        check_arxiv_papers(filename)


if __name__ == "__main__":
    main()
