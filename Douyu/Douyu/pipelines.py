# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import scrapy
from scrapy.pipelines.images import ImagesPipeline


class DouyuPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        image_url = item['vertical_src']
        print ("------------------------")
        print (image_url)
        f = open('D:\images\image.txt', 'a')
        f.writelines(str(image_url)+'\n')
        yield scrapy.Request(str(image_url))

    def item_completed(self, results, item, info):
        """
            result结构:
                [(True,
                  {'checksum': '2b00042f7481c7b056c4b410d28f33cf',
                   'path': 'full/0a79c461a4062ac383dc4fade7bc09f1384a3910.jpg',
                   'url': 'http://www.example.com/files/product1.pdf'}),
                 (False,
                  Failure(...))]
        """
        image_path = [x['path'] for ok, x in results if ok]
        IMAGES_STORE = 'D:/images/'
        # 修改图片保存名称为主播昵称
        # 并将爬取的图片存储在IMAGES_STORE设置的相对路径下，用“full”文件存储
        #item{'nickname': 'mm马果儿','vertical_src': ['https://rpic.douyucdn.cn/amrpic-180622/5080896_2157.jpg']}
        print ("+++++++++++++++")
        nickname = item["nickname"]
        city = item["city"]
        room_id = item["room_id"]
        print (item)

        print (image_path)#['full/ab673a244b4bc04c3bc5cc7383f9bf3f628f9861.jpg']
        os.rename(IMAGES_STORE + "/"+ image_path[0], IMAGES_STORE + "rename/" + city + "_" + nickname + ".jpg")
        #item['imagePath'] = IMAGES_STORE + 'full2' + item["nickname"]
        return item
