from scrapy.spiders import SitemapSpider
from scrapy.linkextractors import LinkExtractor
from ihScraper.items import Article

class IndiahikesSpider(SitemapSpider):
    name = 'indiahikes'
    allowed_domains = ['indiahikes.com']
    sitemap_urls = ['https://www.indiahikes.com/sitemap.xml']
    
    # Now using sitemap instead of using rules List.
    #rules = [Rule(LinkExtractor(allow=r'/((?!:).)*$'), callback='parse_info', follow=True)]

    def parse(self, response):
        article = Article()
        article['title'] = response.xpath('//*[@id="highlights"]/h2[1]/strong/text()').get() or response.xpath('//h1/text()').get() or response.xpath('//h1/i/text()').get() 
        article['url'] = response.url
        article['price'] = response.xpath('/html/body/div[1]/div[1]/div[2]/div/div[1]/div/main/article/div[4]/div/div/div/div[2]/div/div/div[1]/div/span[1]/text()').get()
        return article
        
