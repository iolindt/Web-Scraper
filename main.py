import asyncio
import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import json
import logging

logging.basicConfig(level=logging.INFO)


class AsyncWebScraper:
    def __init__(self, start_url, max_pages=10):
        self.start_url = start_url
        self.max_pages = max_pages
        self.visited = set()
        self.results = []

    async def fetch(self, session, url):
        try:
            async with session.get(url, timeout=10) as response:
                return await response.text()
        except Exception as e:
            logging.warning(f"Failed to fetch {url}: {e}")
            return None

    def parse(self, html, base_url):
        soup = BeautifulSoup(html, "html.parser")

        title = soup.title.string if soup.title else "No title"

        links = []
        for a in soup.find_all("a", href=True):
            full_url = urljoin(base_url, a["href"])
            if self._is_valid_url(full_url):
                links.append(full_url)

        return {
            "url": base_url,
            "title": title,
            "links": links[:10]  # ограничим
        }

    def _is_valid_url(self, url):
        parsed = urlparse(url)
        return parsed.scheme in ("http", "https")

    async def crawl(self):
        queue = asyncio.Queue()
        await queue.put(self.start_url)

        async with aiohttp.ClientSession() as session:
            while not queue.empty() and len(self.visited) < self.max_pages:
                url = await queue.get()

                if url in self.visited:
                    continue

                logging.info(f"Crawling: {url}")
                self.visited.add(url)

                html = await self.fetch(session, url)
                if not html:
                    continue

                data = self.parse(html, url)
                self.results.append(data)

                for link in data["links"]:
                    if link not in self.visited:
                        await queue.put(link)

    def save(self, filename="results.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.results, f, indent=4, ensure_ascii=False)


async def main():
    url = input("Enter start URL: ")
    scraper = AsyncWebScraper(url, max_pages=5)

    await scraper.crawl()
    scraper.save()

    print("Done! Results saved to results.json")


if __name__ == "__main__":
    asyncio.run(main())
