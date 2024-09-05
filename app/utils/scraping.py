import requests
from bs4 import BeautifulSoup

def scrape_content(url: str) -> str:
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.get_text(separator=' ', strip=True)
    except Exception as e:
        print(f"Error scraping URL: {e}")
        return ""