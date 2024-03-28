import requests
from parsel import Selector


class NewsScraper:
    PLUS_URL = "https://www.prnewswire.com"
    URL = "https://www.prnewswire.com/news-releases/news-releases-list/"
    HEADERS = {
        "Accept": "text / html, application / xhtml + xml, application / xml; q = 0.9, image / avif, image / webp, * / *;q = 0.8"
        "Accept-Language" "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3"
        "User-Agent" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0"
    }
    LINK_XPATH = '//a[@class="newsreleaseconsolidatelink display-outline w-100"]/@href'
    TITLE_XPATH = '//div[@class="col-sm-8 col-lg-9 pull-left card"]/h3/text()'
    DESCRIPTION_XPATH = '//p[@class="remove-outline"]/text()'
    IMG_XPATH = '//div[@class="img-ratio-element"]/img/@src'

    def scrape_data(self):
        response = requests.request("GET", url=self.URL, headers=self.HEADERS)
        tree = Selector(text=response.text)
        links = tree.xpath(self.LINK_XPATH).getall()
        new_links = [self.PLUS_URL + link for link in links]
        return new_links


if __name__ == "__main__":
    scraper = NewsScraper()
    scraper.scrape_data()