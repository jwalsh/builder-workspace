import os

import requests
from bs4 import BeautifulSoup

# URL of the webpage
url = "https://www.justice.gov/atr/us-and-plaintiff-states-v-google-llc-2023-trial-exhibits"

# Send a GET request to the webpage
response = requests.get(url)

# If the GET request is successful, the status code will be 200
if response.status_code == 200:
    # Get the content of the response
    page_content = response.content

    # Create a BeautifulSoup object and specify the parser
    soup = BeautifulSoup(page_content, "html.parser")

    # Find all links on the webpage
    links = soup.find_all("a")

    # Create a directory to store the downloaded documents
    documents_dir = "documents"
    if not os.path.exists(documents_dir):
        os.makedirs(documents_dir)

    # Loop through all links and download the documents
    for link in links:
        href = link.get("href")
        if href and href.endswith((".pdf", ".docx", ".doc", ".txt")):
            document_url = href
            if not document_url.startswith("http"):
                document_url = "https://www.justice.gov" + document_url
            document_name = os.path.basename(document_url)
            print(f"Downloading {document_name}...")
            response = requests.get(document_url)
            with open(os.path.join(documents_dir, document_name), "wb") as f:
                f.write(response.content)
            print(f"Downloaded {document_name} successfully!")
else:
    print("Failed to retrieve the webpage. Status code: ", response.status_code)
