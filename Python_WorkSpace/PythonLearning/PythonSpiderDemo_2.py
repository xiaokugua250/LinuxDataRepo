#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-08-26 11:10:30
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
import requests
from bs4 import BeautifulSoup
root_url="http://pyvidemo.org"
index_url=root_url+'/category/50/pycon-us-2014'
def get_video_page_url():
	response=requests.get(index_url)
	soup=BeautifulSoup(response.text,"html5lib")
	return [a.attr.get('href') for a in soup.select('div.video-summary-data a[href^=/video]')]
print(get_video_page_url())