import scrapy

class LianJiaSpader(scrapy.Spider):
    name = "czq"
    start_url = ['http://bj.ganji.com/fang1/chaoyang/']

    def parse(self, response):
        print (response)

        title_list = response.xpath(".//div[@class='f-list-item ']/dl/dd[1]/a/text()").extract()
        price_list = response.xpath(".//div[@class='f-list-item ']/dl/dd[5]/div[1]/span[1]/text()").extract()

        print (title_list)
        print (price_list)