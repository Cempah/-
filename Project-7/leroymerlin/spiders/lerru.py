import scrapy
from scrapy.http import HtmlResponse
from leroymerlin.items import LeroymerlinItem
from scrapy.loader import ItemLoader

class LerruSpider(scrapy.Spider):
    name = 'lerru'
    allowed_domains = ['leroymerlin.ru']

    def __init__(self, query):
        super().__init__()
        self.start_urls = [f'https://leroymerlin.ru/search/?q={query}']

    def parse(self, response: HtmlResponse):
        next_page = response.xpath("//a[@data-qa-pagination-item='right']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        links = response.xpath("//a[@data-qa='product-name']")
        for link in links:
            yield response.follow(link, callback=self.parse_product)


    def parse_product(self, response: HtmlResponse):
        loader = ItemLoader(item=LeroymerlinItem(), response=response)

        loader.add_value('link', response.url)
        loader.add_xpath('name', "//h1/text()")
        loader.add_xpath('price', "//span[@slot='price']/text()")
        loader.add_xpath('all_photos', "//img[@slot='thumbs']/@src")
        yield loader.load_item()

        # link = response.url
        # name = response.xpath("//h1/text()").get()
        # price = response.xpath("//span[@slot='price']/text()").get()
        # all_photos = response.xpath("//img[@slot='thumbs']/@src").getall()
        #
        # yield LeroymerlinItem(link=link,
        #                       name=name,
        #                       price=price,
        #                       all_photos=all_photos)
