import httpx
import asyncio
from parsel import Selector
from database.async_database import AsyncDatabase
from database import sql_queries


class AsyncNewsKGScraper:
    PLUS_URL = "https://24.kg/"
    URL = "https://24.kg/page_{page}/"
    HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0"
    }
    TITLE_XPATH = '//div[@class="title"]/a/span/text()'
    TIME_XPATH = '//div[@class="time"]/text()'
    LINK_XPATH = '//div[@class="title"]/a/@href'

    async def fetch_page(self, client, page):
        url = self.URL.format(page=page)
        response = await client.get(url, timeout=10.0)
        print("страница: ", page)
        if response.status_code == 200:
            return Selector(text=response.text)
        else:
            print(f"Error in page: {response.status_code}")
            response.raise_for_status()

    async def scrape_page(self, selector):
        times = selector.xpath(self.TIME_XPATH).getall()
        titles = selector.xpath(self.TITLE_XPATH).getall()
        links = selector.xpath(self.LINK_XPATH).getall()
        db = AsyncDatabase()
        for title, time, link in zip(titles, times, links):
            await db.execute_query(
                query=sql_queries.INSERT_SCRAP_NEWS_24KG_QUERY,
                params=(
                    None,
                    title,
                    time,
                    self.PLUS_URL+link
                ),
                fetch='none'
            )

    async def get_pages(self, limit=10):
        async with httpx.AsyncClient(headers=self.HEADERS) as client:
            tasks = [self.fetch_page(client, page) for page in range(1, limit + 1)]
            pages = await asyncio.gather(*tasks)
            scraping_tasks = [self.scrape_page(selector=selector) for selector in pages if pages is not None]
            await asyncio.gather(*scraping_tasks)


if __name__ == "__main__":
    scraper = AsyncNewsKGScraper()
    asyncio.run(scraper.get_pages())

