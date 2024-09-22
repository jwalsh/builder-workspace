import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import json
import os
from urllib.robotparser import RobotFileParser
from analyzer.utils.text_processing import check_similarity
from analyzer.utils.file_operations import load_existing_projects

ARXIV_URL = "https://arxiv.org/list/cs.AI/recent"
CACHE_FILE = "arxiv_cache.json"
CACHE_EXPIRY = timedelta(hours=1)
MAX_PAPERS = 3


def get_robots_txt(url):
    rp = RobotFileParser()
    rp.set_url(f"{url}/robots.txt")
    rp.read()
    return rp


def can_fetch(url, rp):
    return rp.can_fetch("*", url)


def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            cache = json.load(f)
        cache["last_updated"] = datetime.fromisoformat(cache["last_updated"])
        return cache
    return {"last_updated": datetime.min, "papers": []}


def save_cache(cache):
    cache["last_updated"] = cache["last_updated"].isoformat()
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f)


def fetch_recent_papers(url, rp):
    cache = load_cache()
    if datetime.now() - cache["last_updated"] < CACHE_EXPIRY:
        return cache["papers"][:MAX_PAPERS]

    if not can_fetch(url, rp):
        print("Fetching is not allowed according to robots.txt")
        return []

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    papers = []
    for dt in soup.find_all("dt")[:MAX_PAPERS]:
        paper = {}
        id_element = dt.find("a", {"title": "Abstract"})
        if id_element:
            paper["id"] = id_element.text.strip()
        else:
            continue

        dd = dt.find_next("dd")
        if dd:
            title_element = dd.find("div", class_="list-title")
            if title_element:
                paper["title"] = title_element.text.replace("Title:", "").strip()
            else:
                paper["title"] = "Title not found"

            abstract_element = dd.find("p", class_="mathjax")
            if abstract_element:
                paper["abstract"] = abstract_element.text.strip()
            else:
                paper["abstract"] = "Abstract not found"
        else:
            continue

        papers.append(paper)

    cache["papers"] = papers
    cache["last_updated"] = datetime.now()
    save_cache(cache)

    return papers


def check_arxiv_papers(filename):
    rp = get_robots_txt(ARXIV_URL)
    papers = fetch_recent_papers(ARXIV_URL, rp)

    if not papers:
        print(
            "No papers fetched. Check if fetching is allowed or if cache is still valid."
        )
        return

    print(f"Fetched {len(papers)} recent papers from arXiv cs.AI:")
    for paper in papers:
        print(f"- {paper.get('title', 'No title')} (arXiv:{paper.get('id', 'No ID')})")

    existing_projects = load_existing_projects(filename)
    similar_projects = check_similarity(papers, existing_projects)

    if similar_projects:
        print("\nSimilar projects found:")
        for paper, project, similarity in similar_projects:
            print(f"arXiv paper: {paper.get('title', 'No title')}")
            print(f"Similar to existing project: {project.get('title', 'No title')}")
            print(f"Similarity score: {similarity:.2f}")
            print()
    else:
        print("\nNo similar projects found.")
