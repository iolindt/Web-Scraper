Scrapes data from a website with BeautifulSoup.
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time


class WebScraper:
    def __init__(self, base_url, delay=1):
        self.base_url = base_url
        self.visited = set()
        self.delay = delay

    def fetch_page(self, url):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"[ERROR] Failed to fetch {url}: {e}")
            return None

    def parse_links(self, html, current_url):
        soup = BeautifulSoup(html, "html.parser")
        links = set()

        for tag in soup.find_all("a", href=True):
            full_url = urljoin(current_url, tag["href"])
            if self.base_url in full_url:
                links.add(full_url)

        return links

    def extract_data(self, html):
        soup = BeautifulSoup(html, "html.parser")

        title = soup.title.string.strip() if soup.title else "No title"

        headings = [h.get_text(strip=True) for h in soup.find_all(["h1", "h2"])]

        return {
            "title": title,
            "headings": headings
        }

    def crawl(self, max_pages=5):
        to_visit = [self.base_url]

        while to_visit and len(self.visited) < max_pages:
            url = to_visit.pop(0)

            if url in self.visited:
                continue

            print(f"[INFO] Crawling: {url}")
            html = self.fetch_page(url)

            if not html:
                continue

            data = self.extract_data(html)
            print(f"[DATA] Title: {data['title']}")
            print(f"[DATA] Headings: {data['headings']}\n")

            self.visited.add(url)

            links = self.parse_links(html, url)
            for link in links:
                if link not in self.visited:
                    to_visit.append(link)

            time.sleep(self.delay)


if __name__ == "__main__":
    url = input("Enter website URL: ").strip()
    scraper = WebScraper(url, delay=1)
    scraper.crawl(max_pages=5)
