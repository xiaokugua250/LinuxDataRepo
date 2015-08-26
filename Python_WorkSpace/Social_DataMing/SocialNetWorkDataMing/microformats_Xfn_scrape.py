#-*- coding:utf-8 -*-
import sys
import urllib2
import HTMLParser
from BeautifulSoup import BeautifulSoup
URL=sys.argv[1]
XFN_TAGS=set([
'colleague','sweetheart','parent','co-resident','co-worker','muse','neigbor','sibling','kin','child','date','spouse','me','acquaintance','met','crush',
 'contact','friend',
])
try:
    page=urllib2.urlopen(URL)
except urllib2.URLError:
        print('failed to parse'+item)
try:
        soup=BeautifulSoup(page)
except Exception :
        print('failed to parse'+item)
anchorTags=soup.findAll('a')
for a in anchorTags:
        if a.has_key('ref'):
                if len(set(a['ref'].split())&XFN_TAGS)>0:
                        tags=a['ref'].split()
                        print(a.contents[0],a['href'],tags)

