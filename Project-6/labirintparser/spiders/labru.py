import scrapy
from scrapy.http import HtmlResponse
from labirintparser.items import LabirintparserItem

class LabruSpider(scrapy.Spider):
    name = 'labru'
    allowed_domains = ['labirint.ru']
    start_urls = ['https://www.labirint.ru/search/%D0%9F%D1%81%D0%B8%D1%85%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%8F/?stype=0',
                  'https://www.labirint.ru/search/%D0%A4%D1%8D%D0%BD%D1%82%D0%B5%D0%B7%D0%B8/?stype=0']


    def parse(self, response: HtmlResponse):
        next_page = response.xpath("//a[@class='pagination-next__text']/@href").get()
        if next_page:
            count = 1
            next_page = next_page[:-1] + str(count)
            count += 1
            yield response.follow(next_page, callback=self.parse)

        links = response.xpath("//a[@class='cover']/@href").getall()
        for link in links:
            yield response.follow(link, callback=self.book_parse)



    def book_parse(self, response: HtmlResponse):
        link_book = response.url
        book_name = response.xpath("//h1/text()").get()
        authors = response.xpath("//a[@data-event-label='author']/text()").getall()
        basic_price = response.xpath("//div[@id='product-info']/@data-price").get()
        discounted_price = response.xpath("//span[@class='buying-pricenew-val-number']/text()").get()
        book_rating = response.xpath("//div[@id='rate']/text()").get()
        item = LabirintparserItem(link_book = link_book,
                                  book_name=book_name,
                                  authors=authors,
                                  basic_price=basic_price,
                                  discounted_price=discounted_price,
                                  book_rating=book_rating)
        yield item
