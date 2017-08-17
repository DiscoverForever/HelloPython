#!/usr/bin/python
# coding=utf-8

"""
@author: tangyueyang
@file: date.py
@time: 2017/7/17 下午5:26
"""
import time
import datetime
import calendar

print time.time()
localtime = time.localtime(time.time())
print time.strftime('%Y-%m-%d %H:%M:%S', localtime)
print 'localtime', time.asctime(localtime)

print calendar.month(2017, 7)

i = datetime.datetime.now()
print ("当前的日期和时间是 %s" % i)
print ("ISO格式的日期和时间是 %s" % i.isoformat() )
print ("当前的年份是 %s" %i.year)
print ("当前的月份是 %s" %i.month)
print ("当前的日期是  %s" %i.day)
print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
print ("当前小时是 %s" %i.hour)
print ("当前分钟是 %s" %i.minute)
print ("当前秒是  %s" %i.second)

