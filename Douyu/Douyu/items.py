# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    vertical_src = scrapy.Field()
    nickname = scrapy.Field()
    imagePath = scrapy.Field()
    city = scrapy.Field()
    room_id = scrapy.Field()
