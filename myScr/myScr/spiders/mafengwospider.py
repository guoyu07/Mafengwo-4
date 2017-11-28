# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from myScr.items import MyscrItem

class MafengwospiderSpider(scrapy.Spider):
    name = 'mafengwospider'
    allowed_domains = ['http://www.mafengwo.cn']
    def start_requests(self):
        #首次爬取模拟成浏览器进行
        yield Request("http://www.mafengwo.cn/search/s.php?q=美国&p=1&t=info&kt=1",headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0"})

    def parse(self, response):
        count=0
        item=MyscrItem()
        item["author"]=response.xpath("//ul[@class='seg-info-list clearfix']/li[last()-1]/a/text()").extract()
        item["publishDate"]=response.xpath("//ul[@class='seg-info-list clearfix']/li[last()]/text()").extract()
        item["detailUrl"]=response.xpath("//div[@class='clearfix']/div[@class='flt1']/a/@href").extract()
        for i in range(0,len(item["detailUrl"])):
        	detailUrl=item["detailUrl"][i]
        	publishDate=item["publishDate"][i]
        	author=item["author"][i]
        	yield Request(url=item["detailUrl"][i],meta={'author':author,'publishDate':publishDate,'detailUrl':detailUrl},callback=self.parse_detail,dont_filter = True)
        

    def parse_detail(self,response):
    	item=MyscrItem()
    	item["author"]=response.meta['author']
    	item["publishDate"]=response.meta['publishDate'].strip()
    	item["detailUrl"]=response.meta['detailUrl']
     
    	item["departureTime"]=response.xpath("//li[@class='time']/text()[2]").extract()
    	item["pireod"]=response.xpath("//li[@class='day']/text()[2]").extract()
    	item["expense"]=response.xpath("//li[@class='cost']/text()[2]").extract()
    	item["place"]=response.xpath("//span[@class='pic_tag']/a/text()").extract()


    	yield item


       	        # 	item["days"][i]=response.xpath("//li[@class='day']/span/following::text()").extract()
        # yield item
        # for i in range(0,len(item["url"])):
        # 	yield Request(item["url"][i],headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0"})
        # 	item["fee"].insert(i+1,response.xpath("//li[@class='cost']/text()").extract()