#!/usr/bin/python  
# coding=utf-8

"""
@author: tangyueyang
@file: spider.py
@time: 2017/7/18 上午9:03
"""
import urllib2, re, threading, time


class Spider:
    def __init__(self):
        self.page = 0

    def get_html(self, url, page):
        try:
            user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' + str(page)
            headers = {'User-Agent': user_agent}
            request = urllib2.Request(url + str(page), headers=headers)
            response = urllib2.urlopen(request)
            return response.read().decode('utf-8')
        except urllib2.URLError, e:
            if hasattr(e, 'code'):
                print e.code
            if hasattr(e, 'reason'):
                print e.reason

    def reset_data(self, html):
        pattern = re.compile(
            '<div.*?author clearfix">.*?<a.*?>.*?<img.*?src="(.*?)".*?>.*?</a>.*?<a.*?>.*?<h2>(.*?)</h2>.*?</a>.*?<div.*?manIcon">(.*?)</div>.*?</div>.*?<a.*?contentHerf.*?>.*?<div.*?content">.*?<span>(.*?)</span>.*?</div>.*?</a>.*?<div.*?thumb">.*?<img.*?src="(.*?)".*?>.*?</a>.*?</div>',
            re.S)
        # 匹配正则容易卡死
        items = re.findall(pattern, html)
        for item in items:
            print '====================='
            print '头像:', item[0]
            print '用户名:', item[1]
            print '年龄:', item[2]
            print '段子:', item[3]
            print '段子图:', item[4]

    def start(self):
        # for i in range(10):
            self.page = self.page + 3
            html = self.get_html('http://www.qiushibaike.com/hot/page/', self.page)
            self.reset_data(html)


Spider().start()

