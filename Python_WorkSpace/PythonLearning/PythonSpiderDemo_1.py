#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-08-26 10:51:22
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
# Python Spider
import Queue
init_page="http://stackoverflow.com/"
url_queue=Queue.Queue()
while(True):
	if url_queue.size()>0:
		current_url=url_queue.get()
		store(current_url)
		for next_url in extract_urls(current_url):
			if next_url not in seen:
				seen.put(next_url)
				url_queue.put(next_url))
	else:
		break