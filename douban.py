#!/usr/bin/python
#-*- coding: utf-8 -*-
#encoding=utf-8

from BeautifulSoup import BeautifulSoup
import requests
import scrapy

douban_url = 'http://moview.douban.com/top250'

def download_page(url):
    data = requests.get(url).content
    return data

def main():
    print download_page(douban_url)

if __name__ == '__main__':
    main()
