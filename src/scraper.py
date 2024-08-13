import requests
from bs4 import BeautifulSoup
import logging 

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class WebScraper:
    def __init__(self, url):
        self.url = url

    def fetch_content(self):
        logger.info(f"Fetching content from {self.url}")
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.content
        else:
            raise Exception(f"Failed to fetch content from {self.url}")

    def parse_content(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        # Exemplo de extração de dados
        data = []
        for item in soup.select('.item-class'):
            title = item.select_one('.title-class').text
            price = item.select_one('.price-class').text
            data.append({'title': title, 'price': price})
        return data