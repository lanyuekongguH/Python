#!/usr/bin/python
#-*- coding: utf-8 -*-
#encoding=utf-8


import urllib
import urllib2
import re
import lxml
import requests
from bs4 import BeautifulSoup
import os



headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
all_url = 'http://www.mzitu.com/all'
start_html = requests.get(all_url,headers = headers)
Soup = BeautifulSoup(start_html.text, 'lxml')
all_a = Soup.find('div', class_='all').find_all('a')
for li in all_a:
    title = li.string
    path = title
    os.makedirs(os.path.join("/Users/damon/Desktop/Data", path))
    os.chdir("/Users/damon/Desktop/Data//" + path)
    href = li['href']
    html = requests.get(href, headers=headers)
    html_Soup = BeautifulSoup(html.text, 'lxml')
    max_span = html_Soup.find('div', class_='pagenavi').find_all('span')[-2].string
    for page in range(1, int(max_span) + 1):
        page_url = href + '/' + str(page)
        imag_html = requests.get(page_url, headers=headers)
        imag_Soup = BeautifulSoup(imag_html.text, 'lxml')
        imag_url = imag_Soup.find('div', class_='main-image').find('img')['src']
        name = imag_url[-9:-4]
        img = requests.get(imag_url, headers=headers)
        f = open(name + '.jpg', 'ab')
        f.write(img.content)
        f.close()
        print imag_url


