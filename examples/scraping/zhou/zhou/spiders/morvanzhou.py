# -*- coding: utf-8 -*-
import scrapy
import re


class MorvanzhouSpider(scrapy.Spider):
    name = 'morvanzhou'
    allowed_domains = ['morvanzhou.github.io']
    start_urls = ['http://morvanzhou.github.io/']

    def parse(self, response):
        yield {     # 返回结果
            'title': response.css('h1::text').extract_first(default='Missing').strip().replace('"', ""),
            'url': response.url,
        }
        # 找到所有链接
        urls = response.css('a::attr(href)').re(r'^/.+?/$')
        for url in urls:
            # 自动过滤和重复
            yield response.follow(url, callback=self.parse)
