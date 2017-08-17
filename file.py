#!/usr/bin/python
# coding=utf-8
"""
@author: tangyueyang
@file: file.py
@time: 2017/7/17 下午5:51
"""
import os

class Test:

    @staticmethod
    def getfile():
        myfile = open('class.py')
        return myfile

    @staticmethod
    def createfile(filepath):
        os.mknod(filepath)


Test.getfile().read()
Test.createfile('test.txt')
