# -*- coding: utf-8 -*-
import scrapy
import json
from Douyu.items import DouyuItem


class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['capi.douyucdn.cn']
    initial_URL = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    offset = 0
    URL = initial_URL + str(offset)
    start_urls = [URL]

    def parse(self, response):
        data = json.loads(response.body)['data']
        for node in data:
            item = DouyuItem()
            item['nickname'] = node['nickname']
            item['vertical_src'] = node['vertical_src']
            item['city'] = node['anchor_city']
            item['room_id'] = node['room_id']
            yield item

        self.offset += 20
        if self.offset < 944:
            self.URL = self.initial_URL + str(self.offset)
            yield scrapy.Request(url=self.URL, callback=self.parse)

