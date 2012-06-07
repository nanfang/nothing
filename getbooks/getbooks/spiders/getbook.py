from scrapy.spider import BaseSpider
from scrapy.http import Request, FormRequest
from scrapy.selector import HtmlXPathSelector
from scrapy.conf import settings
from scrapy.contrib.spidermiddleware.httperror import HttpError
from getbooks.items import BookItem

class GetbookSpider(BaseSpider):
    name = "getbook"
    allowed_domains = ["www.eapoo.com"]
    start_urls =  [
                'http://www.eapoo.com/shopthumdetail/1832/1', 
                'http://www.eapoo.com/shopthumdetail/1832/2',
                'http://www.eapoo.com/shopthumdetail/2495/1',
                'http://www.eapoo.com/shopthumdetail/2495/2',
                'http://www.eapoo.com/shopthumdetail/2559/1',
                'http://www.eapoo.com/shopthumdetail/2559/2',
                'http://www.eapoo.com/shopthumdetail/2453/1',
                'http://www.eapoo.com/shopthumdetail/2453/2',
                'http://www.eapoo.com/shopthumdetail/2453/3',
                'http://www.eapoo.com/shopthumdetail/1906/1',
                'http://www.eapoo.com/shopthumdetail/1906/2',
                'http://www.eapoo.com/shopthumdetail/2103/1',                
                'http://www.eapoo.com/shopthumdetail/2103/2',                
                'http://www.eapoo.com/shopthumdetail/2381/1',                
                'http://www.eapoo.com/shopthumdetail/2381/2',                
                'http://www.eapoo.com/shopthumdetail/2381/3',                
                'http://www.eapoo.com/shopthumdetail/2381/4',                
                'http://www.eapoo.com/shopthumdetail/1929/1',                
                'http://www.eapoo.com/shopthumdetail/1929/2',                
                'http://www.eapoo.com/shopthumdetail/1929/3',                
                ]
    
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        book_links = hxs.select('//div[contains(@class, "thumb")]/a/@href')
        for book_link in book_links:
            yield  Request(book_link.extract())            
        
        download_box = hxs.select('//div[contains(@class, "download_list clearfix")]/input')
        if download_box:
            book_item = BookItem()
            book_item['id'] = download_box.select('./@value').extract()[0]
            book_item['name'] = hxs.select('//h1/text()').extract()[0]
            yield book_item 


