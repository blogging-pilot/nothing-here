# scraper.py
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_website(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all anchor tags
        anchors = soup.find_all('a')
        pages = []
        for anchor in anchors:
            href = anchor.get('href')
            if href and not href.startswith('#'):
                full_url = urljoin(url, href)
                if full_url not in pages:
                    pages.append(full_url)
        
        return pages
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []

