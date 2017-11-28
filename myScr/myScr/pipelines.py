# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json
import re
class MyscrPipeline(object):
	def __init__(self):
		self.file = codecs.open("D:/PythonProject/myScr/myScr.json", "wb", encoding="utf-8")

	def process_item(self, item, spider):
		# for j in range(0,len(item["author"])):
		# 	author = item["author"][j]
		# 	date = item["date"][j]
		# 	url = item["url"][j]
		# 	fee = item["fee"][j]
		# 	details={"author":author,"date":date,"url":url,"fee":fee}
			# days = item["days"][j]
		i=json.dumps(dict(item), ensure_ascii=False)
		line = i + '\n'
		self.file.write(line)
		return item

	def close_spider(self,spider):
		self.file.close()