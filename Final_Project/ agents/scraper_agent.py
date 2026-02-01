import requests
from bs4 import BeautifulSoup
import os

def scrape_page(url):
    response = requests.get(url, timeout=10)
    if response.status_code != 200:
        return ""

    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup(["script", "style", "nav", "footer"]):
        tag.decompose()

    text = soup.get_text(separator=" ")
    return " ".join(text.split())

def save_raw_text(text, filename):
    os.makedirs("data/raw_text", exist_ok=True)
    with open(f"data/raw_text/{filename}", "w", encoding="utf-8") as f:
        f.write(text)
