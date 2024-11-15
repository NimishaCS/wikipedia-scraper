import os
import requests
from bs4 import BeautifulSoup


class WikipediaScraper:
    """
    A class to scrape and save Wikipedia page contents.
    """

    def __init__(self, topic: str):
        """
        Initialize the scraper with a Wikipedia topic.
        :param topic: The topic to scrape from Wikipedia.
        """
        self.base_url = "https://en.wikipedia.org/wiki/"
        self.topic = topic
        self.content = None

    def fetch_page(self):
        """
        Fetch the Wikipedia page for the given topic.
        """
        url = self.base_url + self.topic.replace(" ", "_")
        response = requests.get(url)
        if response.status_code == 200:
            self.content = BeautifulSoup(response.text, 'html.parser')
        else:
            raise Exception(f"Failed to fetch the page: {url}. Status code: {response.status_code}")

    def extract_content(self):
        """
        Extract the main content of the Wikipedia page.
        :return: Extracted text content.
        """
        if not self.content:
            raise Exception("Page content is not fetched. Call fetch_page() first.")
        
        paragraphs = self.content.find_all("p")
        # Use the .get_text() method with the separator to preserve spaces between inline elements.
        return "\n\n".join([para.get_text(" ", strip=True) for para in paragraphs if para.get_text(strip=True)])


    def save_to_file(self, output_path: str):
        """
        Save the extracted content to a text file.
        :param output_path: The path where the content will be saved.
        """
        content = self.extract_content()
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"Content saved to {output_path}")

    @staticmethod
    def generate_filename_from_topic(topic: str) -> str:
        """
        Generate a filename by tokenizing the topic string.
        :param topic: The input topic string.
        :return: Generated filename with .txt extension.
        """
        tokens = topic.split()
        filename = "_".join(tokens) + ".txt"
        return os.path.join(os.getcwd(), filename)
