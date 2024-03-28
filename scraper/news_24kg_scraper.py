import requests
from parsel import Selector
from database.bot_db import Database
import lxml.html
import lxml.html.clean


class NewsKGScraper:
    PLUS_URL = "https://24.kg/"
    URL = "https://24.kg/"
    HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0"
    }
    TITLE_XPATH = '//div[@class="title"]/a/span/text()'
    TIME_XPATH = '//div[@class="time"]/text()'
    LINK_XPATH = '//div[@class="title"]/a/@href'

    def scrape_data(self):
        db = Database()
        response = requests.request("GET", url=self.URL, headers=self.HEADERS)
        tree = Selector(text=response.text)
        times = tree.xpath(self.TIME_XPATH).getall()
        links = tree.xpath(self.LINK_XPATH).getall()
        titles = tree.xpath(self.TITLE_XPATH).getall()
        for title, time, link in zip(titles, times, links):
            db.insert_scrap_news_24kg(
                title=title,
                time=time,
                link=self.PLUS_URL + link
            )


if __name__ == "__main__":
    scraper = NewsKGScraper()
    scraper.scrape_data()
