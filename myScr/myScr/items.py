# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyscrItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # main page field
	  author = scrapy.Field()
	  publishDate = scrapy.Field()
	  detailUrl = scrapy.Field()
	# detail page field
	  departureTime = scrapy.Field()
	  pireod = scrapy.Field()
	  expense = scrapy.Field()
	  place = scrapy.Field()
	  # days = scrapy.Field()
   
