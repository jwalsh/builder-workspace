from analyzer.models.category import CategoryEnum
from analyzer.utils.embedding import get_embedding
from analyzer.utils.text_processing import extract_description
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import numpy as np
import orgparse


def analyze_project_similarity(filename="PROJECTS.org"):
    tree = orgparse.load(filename)
    projects = []
    embeddings = []
    for node in tree[1:]:
        if node.heading:
            description = extract_description(node.body)
            category = node.get_property("CATEGORY", CategoryEnum.UNKNOWN.name)
            projects.append({"name": node.heading, "category": category})
            embeddings.append(get_embedding(description))

    embeddings_array = np.array(embeddings)
    pca = PCA(n_components=2)
    reduced_embeddings = pca.fit_transform(embeddings_array)

    kmeans = KMeans(n_clusters=len(CategoryEnum) - 1)
    clusters = kmeans.fit_predict(embeddings_array)

    plt.figure(figsize=(12, 8))
    scatter = plt.scatter(
        reduced_embeddings[:, 0], reduced_embeddings[:, 1], c=clusters, cmap="viridis"
    )
    plt.title("Project Similarity Clusters")
    plt.colorbar(scatter)

    for i, project in enumerate(projects):
        plt.annotate(
            project["name"],
            (reduced_embeddings[i, 0], reduced_embeddings[i, 1]),
            fontsize=8,
        )

    plt.savefig("project_similarity_clusters.png")
    print(
        "Project similarity analysis completed. See 'project_similarity_clusters.png' for visualization."
    )

    cluster_categories = {i: {} for i in range(len(CategoryEnum) - 1)}
    for i, cluster in enumerate(clusters):
        category = projects[i]["category"]
        if category in cluster_categories[cluster]:
            cluster_categories[cluster][category] += 1
        else:
            cluster_categories[cluster][category] = 1

    print("\nCategory distribution in clusters:")
    for cluster, categories in cluster_categories.items():
        print(f"\nCluster {cluster}:")
        for category, count in sorted(
            categories.items(), key=lambda x: x[1], reverse=True
        ):
            print(f"  {category}: {count}")


def analyze_category_similarity():
    categories = [c.name for c in CategoryEnum if c != CategoryEnum.UNKNOWN]
    category_embeddings = [get_embedding(CategoryEnum[c].value) for c in categories]

    similarity_matrix = cosine_similarity(category_embeddings)
    linkage_matrix = linkage(similarity_matrix, "ward")

    plt.figure(figsize=(10, 7))
    dendrogram(linkage_matrix, labels=categories, leaf_rotation=90)
    plt.title("Category Similarity Dendrogram")
    plt.tight_layout()
    plt.savefig("category_similarity_dendrogram.png")

    print(
        "Category similarity analysis completed. See 'category_similarity_dendrogram.png' for visualization."
    )

    threshold = 0.9
    print("\nHighly similar categories (similarity > 0.9):")
    for i in range(len(categories)):
        for j in range(i + 1, len(categories)):
            if similarity_matrix[i][j] > threshold:
                print(
                    f"{categories[i]} and {categories[j]}: {similarity_matrix[i][j]:.2f}"
                )
