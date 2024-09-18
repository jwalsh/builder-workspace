import orgparse
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import cosine_similarity
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt
import requests
from typing import List, Dict, Tuple
from enum import Enum
import click
import google.generativeai as genai
import os
import socket
from datetime import datetime, timedelta
import ast
import astor
import inspect
from collections import Counter
import sys
import csv
import logging
import traceback
from bs4 import BeautifulSoup
from urllib.robotparser import RobotFileParser
import json
from sklearn.feature_extraction.text import TfidfVectorizer
logging.basicConfig(level=logging.DEBUG, format=
    '%(asctime)s - %(levelname)s - %(message)s')
genai.configure(api_key=os.environ['GOOGLE_AI_API_KEY'])
ARXIV_URL = 'https://arxiv.org/list/cs.AI/recent'
CACHE_FILE = 'arxiv_cache.json'
CACHE_EXPIRY = timedelta(hours=1)
MAX_PAPERS = 3


class CategoryEnum(str, Enum):
    AI_ML = (
        'Artificial intelligence and machine learning technologies and applications.'
        )
    AUTOMATION = 'Systems automating complex tasks across various industries.'
    AUTONOMOUS_SYSTEMS = (
        'Technologies for autonomous vehicles, drones, and self-operating systems.'
        )
    BIOTECH = (
        'Biotechnology, genetic engineering, and biocomputing applications.')
    BLOCKCHAIN = 'Solutions enhancing blockchain applications and security.'
    DOCUMENTATION = (
        'Tools for generating and maintaining technical documentation.')
    EDUCATION = 'Solutions aimed at education and personalized learning paths.'
    ENERGY = 'Energy production, distribution, and optimization technologies.'
    ENVIRONMENTAL = (
        'Environmental protection and climate change mitigation technologies.')
    FINANCE = (
        'Applications for financial analysis, fraud detection, and predictions.'
        )
    FORENSICS = 'Applied to digital forensics and investigative analysis.'
    GAMING = (
        'Technologies used in gaming, simulations, and interactive experiences.'
        )
    HCI = 'Human-computer interaction and advanced user interfaces.'
    HEALTHCARE = (
        'Applications improving healthcare diagnostics and patient care.')
    HR = (
        'Human Resources technologies for workforce management and development.'
        )
    INFRASTRUCTURE = (
        'Innovations in construction, infrastructure, and system architecture.'
        )
    IOT = 'Internet of Things technologies for interconnected smart systems.'
    LOGISTICS = 'Optimizing supply chain, transport, and logistics.'
    MARKETING = (
        'Technologies for marketing, customer insights, and personalization.')
    ORCHESTRATION = (
        'Tools for orchestrating processes and services across platforms.')
    QUANTUM = 'Quantum computing innovations and applications.'
    REAL_ESTATE = (
        'Tools for managing and analyzing real estate and housing markets.')
    SECURITY = (
        'Solutions for enhancing security measures, including cybersecurity.')
    SOCIAL_MEDIA = (
        'Platforms for social networking, community building, and digital communication.'
        )
    SPACE = 'Space exploration, satellite systems, and related technologies.'
    SUSTAINABILITY = (
        'Solutions for sustainable development and energy optimization.')
    TRANSPORT = 'Transportation systems and mobility solutions.'
    TRAVEL = (
        'Technologies related to travel, tourism, and hospitality industries.')
    XR = 'Extended reality technologies, including VR, AR, and MR experiences.'
    UNKNOWN = 'Unclassified or unknown category.'
    ADVANCED_MATERIALS = (
        'Nanomaterials, metamaterials, and smart materials with programmable properties.'
        )
    AGRICULTURAL = (
        'Agtech including precision farming, vertical farming, agri-robotics, and AI crop management.'
        )
    ALGORITHMS_AND_ARCHITECTURES = (
        'Advanced algorithms, quantum computing, and novel computational paradigms.'
        )
    BCI = (
        'Brain-computer interfaces for direct communication between the brain and external devices.'
        )
    BIO_ENHANCEMENT = (
        'Biotech for human enhancement, including genetic engineering and synthetic biology.'
        )
    CLOUD = (
        'Cloud computing infrastructure, PaaS, SaaS, and related distributed computing technologies.'
        )
    COGNITIVE_ENHANCEMENT = (
        'Brain-computer interfaces, neurofeedback systems, and cognitive training tools.'
        )
    COMMUNICATIONS = (
        'Advanced telecom, 5G and beyond, satellite comms, and emerging network protocols.'
        )
    ENTERTAINMENT = (
        'Entertainment and education tech, from interactive media and gaming to e-learning platforms.'
        )
    HUMAN_AUGMENTATION = (
        'AI-powered systems for enhancing human capabilities and decision-making.'
        )
    IMMERSIVE = (
        'VR, AR, MR, and other technologies blending digital and physical worlds.'
        )
    INTEGRATION = (
        'Cross-account integration for seamless data and process integration across systems.'
        )
    INTERNET = (
        'Web technologies, internet protocols, CDNs, and internet infrastructure innovations.'
        )
    LEGAL = (
        'Legal tech for contract analysis, compliance, research, and AI-assisted legal services.'
        )
    MANUFACTURING = (
        'Advanced manufacturing tech including smart factories, 3D printing, robotics, and Industry 4.0.'
        )
    MILITARY = (
        'Defense tech including advanced weapons, cybersecurity, and military AI applications.'
        )
    MIND_INTERFACES = (
        'Direct neural interfaces, thought-controlled devices, and brain-computer interaction systems.'
        )
    NEURAL_INTERFACES = (
        'Technologies connecting the human nervous system with external devices or systems.'
        )
    PERSONAL_ENHANCEMENT = (
        'Wearables, health tracking, cognitive training, and lifestyle optimization tools.'
        )
    PHILOSOPHY = (
        'Ethical frameworks and philosophical implications of advanced technologies.'
        )
    RENEWABLE_ENERGY = (
        'Sustainable energy solutions including solar, wind, geothermal, and energy storage.'
        )
    SIMULATION = (
        'Engineering and simulation tech for modeling, digital twins, and virtual testing environments.'
        )
    SOFTWARE_ENGINEERING = (
        'App development tech, languages, frameworks, DevOps tools, and software engineering practices.'
        )
    URBAN = (
        'Smart city tech, intelligent transportation, urban planning, and smart infrastructure.'
        )
    VIRTUALIZATION = (
        'Virtual and cloud computing, including server virtualization and container technologies.'
        )
    WEARABLE = (
        'Smart watches, fitness trackers, AR glasses, and other body-worn smart devices.'
        )
    SCIENCE = (
        'Engineering and scientific research technologies, including advanced laboratory equipment, data analysis tools for scientific research, simulation software for complex scientific phenomena, and innovations in experimental design and execution. This category covers technologies that accelerate scientific discovery, enhance research methodologies, and bridge the gap between theoretical and applied sciences across various disciplines such as physics, chemistry, biology, and interdisciplinary fields.'
        )
    PRODUCTIVITY = (
        'Personal productivity tools and technologies, encompassing task management systems, time-tracking applications, focus-enhancing software, collaborative platforms, and smart personal assistants. This category includes innovations aimed at optimizing individual and team productivity, streamlining workflows, reducing cognitive load, and enhancing decision-making processes in both personal and professional contexts.'
        )
    INNOVATION = (
        'Innovation-driven technologies, including idea generation systems, predictive innovation platforms, advanced design tools, and technologies that facilitate creative problem-solving. This category covers applications that augment human creativity, accelerate the innovation process, identify emerging trends and opportunities, and enable rapid prototyping and testing of new concepts across various industries and domains.'
        )
    WELLBEING = (
        'Technologies for personal and community wellbeing, including mental health support systems, meditation and mindfulness apps, personalized health and fitness coaches, and community health management platforms. This category encompasses innovations that improve physical, mental, and emotional health, promote work-life balance, and enhance overall quality of life for individuals and communities.'
        )
    ACCESSIBILITY = (
        'Advanced accessibility solutions, including adaptive interfaces, real-time translation and captioning systems, navigation aids for the visually impaired, and cognitive assistance tools. This category covers technologies that break down barriers for people with disabilities, enhance digital and physical accessibility, and promote inclusive design in products, services, and environments.'
        )
    ARTS = (
        'Art and culture technologies, including computer-assisted creative tools, digital art platforms, cultural heritage preservation systems, and immersive cultural experiences. This category encompasses innovations that blend technology with artistic expression, facilitate cultural exchange, preserve and digitize cultural artifacts, and create new forms of interactive and generative art.'
        )
    PETS = (
        'Pet care and animal welfare technologies, including smart pet health monitoring systems, automated pet care devices, behavior analysis tools for animals, and platforms for pet services. This category covers innovations that enhance the well-being of pets and other animals, assist pet owners in providing better care, and advance veterinary medicine and animal science.'
        )
    RETAIL = (
        'Retail automation and smart shopping technologies, including intelligent inventory management systems, personalized shopping assistants, automated checkout solutions, and predictive demand forecasting tools. This category encompasses innovations that transform the retail experience, optimize supply chain operations, enhance customer engagement, and enable data-driven decision-making in the retail sector.'
        )
    CONSTRUCTION = (
        'Advanced technologies for building design, construction processes, and infrastructure development.'
        )
    MUSIC = (
        'Innovative technologies for music creation, production, distribution, and interactive experiences.'
        )
    ARTIFICIAL_INTELLIGENCE = 'New category: ARTIFICIAL_INTELLIGENCE'
    REAL_TIME = 'New category: REAL_TIME'
    NEURAL_ENGINEERING = 'New category: NEURAL_ENGINEERING'
    QUANTUM_COMPUTING_AND_SECURITY = (
        'New category: QUANTUM_COMPUTING_AND_SECURITY')
    AUGMENTED_AND_VIRTUAL_REALITY = (
        'New category: AUGMENTED_AND_VIRTUAL_REALITY')
    ARTIFICIAL_INTELLIGENCE_SYSTEMS = (
        'New category: ARTIFICIAL_INTELLIGENCE_SYSTEMS')
    EDUCATION_AND_TRAINING = 'New category: EDUCATION_AND_TRAINING'
    FINANCE_AND_BANKING = 'New category: FINANCE_AND_BANKING'


def get_embedding(text: str) ->List[float]:
    """
    Get the embedding vector for the given text using the Ollama API.
    """
    url = 'http://localhost:11434/api/embeddings'
    payload = {'model': 'mxbai-embed-large', 'prompt': text}
    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()['embedding']


def show_categories():
    """
    Show categories using AST, sorted by frequency of usage in the PROJECTS.org file.
    Display warnings for over- and under-utilized categories.
    """
    export_categories_to_csv(CategoryEnum, 'categories.csv')
    module = ast.parse(inspect.getsource(__import__(__name__)))
    enum_class_def = next((node for node in module.body if isinstance(node,
        ast.ClassDef) and node.name == 'CategoryEnum'), None)
    if enum_class_def:
        categories = [node.targets[0].id for node in enum_class_def.body if
            isinstance(node, ast.Assign)]
        tree = orgparse.load('PROJECTS.org')
        category_usage = Counter()
        total_projects = 0
        for node in tree[1:]:
            if node.heading:
                total_projects += 1
                category = node.get_property('CATEGORY', '')
                if category in categories:
                    category_usage[category] += 1
        avg_usage = total_projects / len(categories)
        over_threshold = avg_usage * 1.5
        under_threshold = avg_usage * 0.5
        sorted_categories = sorted(categories, key=lambda x: category_usage
            .get(x, 0), reverse=True)
        print(
            f'Categories (sorted by usage frequency, average usage: {avg_usage:.2f}):'
            )
        for category in sorted_categories:
            count = category_usage.get(category, 0)
            status = ''
            if count > over_threshold:
                status = ' [OVER-UTILIZED]'
            elif count < under_threshold:
                status = ' [UNDER-UTILIZED]'
            print(
                f"- {category}: {count} {'use' if count == 1 else 'uses'}{status}"
                )
        over_utilized = [c for c in categories if category_usage.get(c, 0) >
            over_threshold]
        under_utilized = [c for c in categories if category_usage.get(c, 0) <
            under_threshold]
        if over_utilized:
            print('\nWarning: The following categories are over-utilized:')
            for category in over_utilized:
                print(f'- {category}')
        if under_utilized:
            print('\nWarning: The following categories are under-utilized:')
            for category in under_utilized:
                print(f'- {category}')
    else:
        print('CategoryEnum not found')


def extract_description(body: str) ->str:
    """
    Extract the description from the node body.
    """
    lines = body.strip().splitlines()
    for line in lines:
        if line.startswith('#+begin_src txt :tangle'):
            continue
        if line.startswith('#+end_src'):
            break
        return line.strip()
    return ''


def categorize_description(model, description: str, priority_categories:
    List[str]) ->str:
    """
    Categorize a project description into a CategoryEnum using Gemini.
    Prioritize under-utilized categories.
    """
    categories = [category.name for category in CategoryEnum if category !=
        CategoryEnum.UNKNOWN]
    priority_categories_str = ', '.join(priority_categories
        ) if priority_categories else 'None'
    prompt = f"""Which category does this project description belong to? Choose one from the following options: {', '.join(categories)}. 
    Prioritize these under-utilized categories if appropriate: {priority_categories_str}
    Description: {description}"""
    response = model.generate_content(prompt)
    category_name = response.text.strip().upper()
    return (category_name if category_name in CategoryEnum.__members__ else
        CategoryEnum.UNKNOWN.name)


def suggest_new_categories(model, uncategorized_projects: List[Dict[str, str]]
    ) ->List[str]:
    """
    Suggest new categories based on uncategorized projects.
    """
    prompt = (
        f'Based on these uncategorized projects: {uncategorized_projects}, suggest up to 3 new categories. Return the suggestions as a Python list of uppercase strings with underscores as a delimiter.'
        )
    print(prompt)
    response = model.generate_content(prompt)
    print(response.text)
    try:
        return ast.literal_eval(response.text)
    except:
        print('Error parsing AI response for new categories. Using empty list.'
            )
        return []


def update_category_enum(new_categories: List[str]):
    """
    Update the CategoryEnum with new categories using AST.
    """
    global CategoryEnum
    module = ast.parse(inspect.getsource(sys.modules[__name__]))
    enum_class = next((node for node in module.body if isinstance(node, ast
        .ClassDef) and node.name == 'CategoryEnum'), None)
    if enum_class:
        existing_categories = {node.targets[0].id: node.value.s for node in
            enum_class.body if isinstance(node, ast.Assign)}
        for category in new_categories:
            if category not in existing_categories:
                new_assign = ast.Assign(targets=[ast.Name(id=category, ctx=
                    ast.Store())], value=ast.Str(s=f'New category: {category}')
                    )
                enum_class.body.append(new_assign)
        new_enum_dict = {name: value for name, value in existing_categories
            .items()}
        new_enum_dict.update({category: f'New category: {category}' for
            category in new_categories if category not in existing_categories})
        CategoryEnum = Enum('CategoryEnum', new_enum_dict)
        updated_source = astor.to_source(module)
        with open(__file__, 'w') as file:
            file.write(updated_source)
        print(
            f"CategoryEnum updated with new categories: {', '.join(new_categories)}"
            )
    else:
        print('Error: CategoryEnum not found in the source code.')


def export_categories_to_csv(categories: Enum, output_file: str):
    """Exports categories from an Enum to a CSV file for AWS Comprehend classifier."""
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Category', 'Description'])
        for category in categories:
            writer.writerow([category.name, category.value])


def get_category_usage(filename='PROJECTS.org') ->Tuple[Dict[str, int], float]:
    """
    Get the usage count of each category and the average usage.
    """
    tree = orgparse.load(filename)
    category_usage = Counter()
    total_projects = 0
    for node in tree[1:]:
        if node.heading:
            total_projects += 1
            category = node.get_property('CATEGORY', '')
            if category in CategoryEnum.__members__:
                category_usage[category] += 1
    avg_usage = total_projects / len(CategoryEnum.__members__)
    return category_usage, avg_usage


def get_category_embedding(category: str) ->List[float]:
    """
    Get the embedding for a category description.
    """
    return get_embedding(CategoryEnum[category].value)


def analyze_category_similarity():
    """
    Analyze the similarity between categories using embeddings.
    """
    categories = [c.name for c in CategoryEnum if c != CategoryEnum.UNKNOWN]
    category_embeddings = [get_category_embedding(c) for c in categories]
    similarity_matrix = cosine_similarity(category_embeddings)
    linkage_matrix = linkage(similarity_matrix, 'ward')
    plt.figure(figsize=(10, 7))
    dendrogram(linkage_matrix, labels=categories, leaf_rotation=90)
    plt.title('Category Similarity Dendrogram')
    plt.tight_layout()
    plt.savefig('category_similarity_dendrogram.png')
    print(
        "Category similarity analysis completed. See 'category_similarity_dendrogram.png' for visualization."
        )
    threshold = 0.9
    print('\nHighly similar categories (similarity > 0.9):')
    for i in range(len(categories)):
        for j in range(i + 1, len(categories)):
            if similarity_matrix[i][j] > threshold:
                print(
                    f'{categories[i]} and {categories[j]}: {similarity_matrix[i][j]:.2f}'
                    )


def update_readme(tree, is_dirty, filename='PROJECTS.org'):
    """
    Update the PROJECTS.org file if changes were made, using a tmp file for safety.
    """
    if is_dirty:
        original_project_count = len([node for node in tree[1:] if node.
            heading])
        username = os.environ.get('USER')
        hostname = socket.gethostname()
        current_date = datetime.now().strftime('%Y-%m-%d')
        valid_categories = set(c.name for c in CategoryEnum if c !=
            CategoryEnum.UNKNOWN)
        projects = []
        for node in tree[1:]:
            if node.heading:
                category = node.get_property('CATEGORY', '')
                if category not in valid_categories:
                    category = CategoryEnum.UNKNOWN.name
                projects.append((category, node.heading, node))
        projects.sort(key=lambda x: (x[0], x[1]))
        with open('PROJECTS.tmp', 'w') as f:
            f.write('#+TITLE: Project Repository\n')
            f.write(f'#+AUTHOR: {username}@{hostname}\n')
            f.write(f'#+DATE: {current_date}\n')
            f.write('#+OPTIONS: toc:nil num:nil\n\n')
            for category, _, node in projects:
                f.write('\n')
                f.write(f'* {node.heading}\n')
                f.write(f'  :PROPERTIES:\n')
                f.write(f'  :CATEGORY: {category}\n')
                f.write(f"  :CREATED: {node.get_property('CREATED', '')}\n")
                f.write(f"  :UPDATED: {node.get_property('UPDATED', '')}\n")
                f.write(
                    f"  :UPDATED_BY: {node.get_property('UPDATED_BY', '')}\n")
                f.write(f'  :END:\n')
                f.write(node.body)
        tmp_tree = orgparse.load('PROJECTS.tmp')
        tmp_project_count = len([node for node in tmp_tree[1:] if node.heading]
            )
        if tmp_project_count == original_project_count:
            os.replace('PROJECTS.tmp', filename)
            print(f'{filename} updated.')
        else:
            print(
                f'Error: Project count mismatch {tmp_project_count} vs. {original_project_count}. {filename} not updated. PROJECTS.tmp retained for inspection.'
                )
        return True
    else:
        print(f'No changes made to {filename}.')
        return False


def export_projects_to_csv(output_file: str, filename='PROJECTS.org'):
    """
    Export projects with their categories and descriptions to a CSV file.
    """
    try:
        logging.info(f'Starting export to {output_file}')
        tree = orgparse.load(filename)
        logging.debug(f'Loaded {filename}, found {len(tree)} nodes')
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Category', 'Project Name', 'Description'])
            for node in tree[1:]:
                if node.heading:
                    category = node.get_property('CATEGORY', CategoryEnum.
                        UNKNOWN.name)
                    description = extract_description(node.body)
                    writer.writerow([category, node.heading, description])
                    logging.debug(f'Wrote project: {node.heading}')
        logging.info(f'Projects exported to {output_file}')
    except Exception as e:
        logging.error(f'Error in export_projects_to_csv: {str(e)}')
        logging.debug(traceback.format_exc())


def split_data_for_training(input_file: str, train_file: str, test_file:
    str, test_split: float=0.2):
    """
    Split the data into training and testing sets.
    """
    try:
        logging.info(f'Splitting data from {input_file}')
        with open(input_file, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)
            data = list(reader)
        np.random.shuffle(data)
        split_index = int(len(data) * (1 - test_split))
        train_data = data[:split_index]
        test_data = data[split_index:]
        with open(train_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(train_data)
        with open(test_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(test_data)
        logging.info(f'Data split into {train_file} and {test_file}')
    except Exception as e:
        logging.error(f'Error in split_data_for_training: {str(e)}')
        logging.debug(traceback.format_exc())


def categorize_projects(max_refresh=3, max_unknown=5, filename='PROJECTS.org'):
    """
    Classify the projects into categories and update the org file.
    Prioritize recategorizing projects from over-utilized categories into under-utilized ones.
    """
    refresh_count = 0
    while refresh_count < max_refresh:
        tree = orgparse.load(filename)
        original_project_count = len([node for node in tree[1:] if node.
            heading])
        is_dirty = False
        unknown_count = 0
        uncategorized_projects = []
        print(f'Loaded {original_project_count} projects from {filename}')
        print(f'Categorization attempt {refresh_count + 1} of {max_refresh}')
        model = genai.GenerativeModel('gemini-pro')
        category_usage, avg_usage = get_category_usage(filename)
        over_threshold = avg_usage * 1.5
        under_threshold = avg_usage * 0.5
        over_utilized = [c for c, count in category_usage.items() mif count >
            over_threshold]
        under_utilized = [c for c, count in category_usage.items() if count <
            under_threshold]
        for node in tree[1:]:
            if node.heading:
                category = node.get_property('CATEGORY', '')
                description = extract_description(node.body)
                should_recategorize = (not category or category not in
                    CategoryEnum.__members__ or category == 'UNKNOWN' or 
                    category in over_utilized and under_utilized)
                if should_recategorize:
                    if unknown_count < max_unknown:
                        print(f'\nCategorizing project: {node.heading}')
                        print(f'Description: {description}')
                        print(f'Current Category: {category}')
                        try:
                            category_new = categorize_description(model,
                                description, under_utilized)
                            if category_new != category:
                                print(
                                    f'Updating category from {category} to {category_new}'
                                    )
                                node.properties['CATEGORY'] = category_new
                                node.properties['UPDATED_BY'] = (
                                    f"{os.environ.get('USER')}@{socket.gethostname()}"
                                    )
                                node.properties['UPDATED'] = datetime.now(
                                    ).strftime('%Y-%m-%d %H:%M:%S')
                                is_dirty = True
                            else:
                                print(f'Category remains unchanged: {category}'
                                    )
                                uncategorized_projects.append({'name': node
                                    .heading, 'description': description})
                        except Exception as e:
                            print(f'Error: {e}')
                            uncategorized_projects.append({'name': node.
                                heading, 'description': description})
                        unknown_count += 1
                    else:
                        print(
                            f'Skipping categorization for {node.heading} (max unknown limit reached)'
                            )
                        uncategorized_projects.append({'name': node.heading,
                            'description': description})
                else:
                    print(
                        f'Skipping categorization for {node.heading} (already categorized as {category})'
                        )
        changes_made = update_readme(tree, is_dirty, filename)
        if uncategorized_projects:
            new_categories = suggest_new_categories(model,
                uncategorized_projects)
            if new_categories:
                print(f'Suggested new categories: {new_categories}')
                update_category_enum(new_categories)
                print('CategoryEnum updated. Rerunning categorization.')
                refresh_count += 1
                continue
        if changes_made:
            print(
                f'Changes made. Processed {unknown_count} unknown categories.')
            refresh_count += 1
        else:
            print('No changes made.')
            break
        if unknown_count < max_unknown:
            print('All unknown categories processed. Stopping categorization.')
            break
    if refresh_count == max_refresh:
        print(
            f'Reached maximum number of category refreshes ({max_refresh}). Stopping categorization.'
            )
    export_projects_to_csv('category_projects_for_test_training.csv', filename)


def analyze_project_similarity(filename='PROJECTS.org'):
    """
    Analyze project similarity using embeddings.
    """
    tree = orgparse.load(filename)
    projects = []
    embeddings = []
    for node in tree[1:]:
        if node.heading:
            description = extract_description(node.body)
            category = node.get_property('CATEGORY', CategoryEnum.UNKNOWN.name)
            projects.append({'name': node.heading, 'category': category})
            embeddings.append(get_embedding(description))
    embeddings_array = np.array(embeddings)
    pca = PCA(n_components=2)
    reduced_embeddings = pca.fit_transform(embeddings_array)
    kmeans = KMeans(n_clusters=len(CategoryEnum) - 1)
    clusters = kmeans.fit_predict(embeddings_array)
    plt.figure(figsize=(12, 8))
    scatter = plt.scatter(reduced_embeddings[:, 0], reduced_embeddings[:, 1
        ], c=clusters, cmap='viridis')
    plt.title('Project Similarity Clusters')
    plt.colorbar(scatter)
    for i, project in enumerate(projects):
        plt.annotate(project['name'], (reduced_embeddings[i, 0],
            reduced_embeddings[i, 1]), fontsize=8)
    plt.savefig('project_similarity_clusters.png')
    print(
        "Project similarity analysis completed. See 'project_similarity_clusters.png' for visualization."
        )
    cluster_categories = {i: {} for i in range(len(CategoryEnum) - 1)}
    for i, cluster in enumerate(clusters):
        category = projects[i]['category']
        if category in cluster_categories[cluster]:
            cluster_categories[cluster][category] += 1
        else:
            cluster_categories[cluster][category] = 1
    print('\nCategory distribution in clusters:')
    for cluster, categories in cluster_categories.items():
        print(f'\nCluster {cluster}:')
        for category, count in sorted(categories.items(), key=lambda x: x[1
            ], reverse=True):
            print(f'  {category}: {count}')


def get_robots_txt(url):
    rp = RobotFileParser()
    rp.set_url(f'{url}/robots.txt')
    rp.read()
    return rp


def can_fetch(url, rp):
    return rp.can_fetch('*', url)


def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as f:
            cache = json.load(f)
        cache['last_updated'] = datetime.fromisoformat(cache['last_updated'])
        return cache
    return {'last_updated': datetime.min, 'papers': []}


def save_cache(cache):
    cache['last_updated'] = cache['last_updated'].isoformat()
    with open(CACHE_FILE, 'w') as f:
        json.dump(cache, f)


def fetch_recent_papers(url, rp):
    cache = load_cache()
    if datetime.now() - cache['last_updated'] < CACHE_EXPIRY:
        return cache['papers'][:MAX_PAPERS]
    if not can_fetch(url, rp):
        print('Fetching is not allowed according to robots.txt')
        return []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    papers = []
    for dt in soup.find_all('dt')[:MAX_PAPERS]:
        paper = {}
        paper['id'] = dt.find('a', {'title': 'Abstract'}).text.strip()
        dd = dt.find_next('dd')
        paper['title'] = dd.find('div', class_='list-title').text.replace(
            'Title:', '').strip()
        paper['abstract'] = dd.find('p', class_='mathjax').text.strip()
        papers.append(paper)
    cache['papers'] = papers
    cache['last_updated'] = datetime.now()
    save_cache(cache)
    return papers


def check_similarity(papers, existing_projects):
    all_texts = [(p['title'] + ' ' + p['abstract']) for p in papers] + [(p[
        'title'] + ' ' + p.get('description', '')) for p in existing_projects]
    vectorizer = TfidfVectorizer().fit_transform(all_texts)
    cosine_similarities = cosine_similarity(vectorizer)
    similar_projects = []
    for i, paper in enumerate(papers):
        paper_similarities = cosine_similarities[i, len(papers):]
        most_similar_idx = paper_similarities.argmax()
        if paper_similarities[most_similar_idx] > 0.3:
            similar_projects.append((paper, existing_projects[
                most_similar_idx], paper_similarities[most_similar_idx]))
    return similar_projects


def load_existing_projects(filename='PROJECTS.org'):
    tree = orgparse.load(filename)
    projects = []
    for node in tree[1:]:
        if node.heading:
            projects.append({'title': node.heading, 'description':
                extract_description(node.body), 'category': node.
                get_property('CATEGORY', '')})
    return projects


def deduplicate_projects(filename='PROJECTS.org'):
    """
    Identify and merge similar projects based on their descriptions.
    """
    tree = orgparse.load(filename)
    projects = []
    for node in tree[1:]:
        if node.heading:
            description = extract_description(node.body)
            projects.append({'name': node.heading, 'description':
                description, 'node': node, 'embedding': get_embedding(
                description)})
    similarity_threshold = 0.9
    merged_projects = []
    for i, project in enumerate(projects):
        if project in merged_projects:
            continue
        similar_projects = []
        for j, other_project in enumerate(projects[i + 1:]):
            if other_project in merged_projects:
                continue
            similarity = cosine_similarity([project['embedding']], [
                other_project['embedding']])[0][0]
            if similarity > similarity_threshold:
                similar_projects.append(other_project)
        if similar_projects:
            print(f"Found similar projects to '{project['name']}'. Merging:")
            for similar_project in similar_projects:
                print(f"- {similar_project['name']}")
                project['node'].body += f"""
* Merged from '{similar_project['name']}'
{similar_project['node'].body}"""
                tree.remove(similar_project['node'])
            merged_projects.extend(similar_projects)
    if merged_projects:
        update_readme(tree, True, filename)
        print(f'Merged {len(merged_projects)} similar projects.')
    else:
        print('No similar projects found for merging.')


@click.command()
@click.option('--action', type=click.Choice(['categorize', 'analyze',
    'categories', 'export', 'train-test', 'deduplicate', 'check-arxiv']),
    default='categorize', help='Action to perform')
@click.option('--max-refresh', type=int, default=3, help=
    'Maximum number of times to refresh categories and re-run categorization.')
@click.option('--max-unknown', type=int, default=5, help=
    'Maximum number of unknown categories to process during categorization.')
@click.option('--output-file', type=str, default=
    'projects_for_training.csv', help='Output file name for CSV export.')
@click.option('--train-file', type=str, default='train_data.csv', help=
    'Output file name for training data.')
@click.option('--test-file', type=str, default='test_data.csv', help=
    'Output file name for test data.')
@click.option('--test-split', type=float, default=0.2, help=
    'Proportion of data to use for testing (0.0 to 1.0).')
@click.option('--filename', type=str, default='PROJECTS.org', help=
    'Input org file name.')
def main(action: str, max_refresh: int, max_unknown: int, output_file: str,
    train_file: str, test_file: str, test_split: float, filename: str):
    try:
        if action == 'categorize':
            categorize_projects(max_refresh, max_unknown, filename)
        elif action == 'analyze':
            analyze_project_similarity(filename)
            analyze_category_similarity()
        elif action == 'categories':
            show_categories()
        elif action == 'export':
            export_projects_to_csv(output_file, filename)
        elif action == 'train-test':
            export_projects_to_csv(output_file, filename)
            split_data_for_training(output_file, train_file, test_file,
                test_split)
        elif action == 'deduplicate':
            deduplicate_projects(filename)
        elif action == 'check-arxiv':
            rp = get_robots_txt(ARXIV_URL)
            papers = fetch_recent_papers(ARXIV_URL, rp)
            if not papers:
                print(
                    'No papers fetched. Check if fetching is allowed or if cache is still valid.'
                    )
                return
            existing_projects = load_existing_projects(filename)
            similar_projects = check_similarity(papers, existing_projects)
            print(f'Fetched {len(papers)} recent papers from arXiv cs.AI:')
            for paper in papers:
                print(f"- {paper['title']} (arXiv:{paper['id']})")
            if similar_projects:
                print('\nSimilar projects found:')
                for paper, project, similarity in similar_projects:
                    print(f"arXiv paper: {paper['title']}")
                    print(f"Similar to existing project: {project['title']}")
                    print(f'Similarity score: {similarity:.2f}')
                    print()
            else:
                print('\nNo similar projects found.')
    except Exception as e:
        logging.error(f'Error in main function: {str(e)}')
        logging.debug(traceback.format_exc())


if __name__ == '__main__':
    main()
