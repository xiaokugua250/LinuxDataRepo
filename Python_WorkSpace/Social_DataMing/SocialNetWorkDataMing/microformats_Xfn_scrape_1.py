#-*- coding:utf-8 -*-
import sys
import urllib2
import os
import HTMLParser
import requests
import networkx as nx
from BeautifulSoup import BeautifulSoup
ROOT_URL=sys.argv[1]
if len(sys.argv)>2:
        MAX_DEPTH=int(sys.argv[2])
else:
        MAX_DEPTH=1
XFN_TAGS=set([
'colleague','sweetheart','parent','co-resident','co-worker','muse','neigbor','sibling','kin','child','date','spouse','me','acquaintance','met','crush',
 'contact','friend',
])
OUT="graph.dot"
depth=0
g=nx.DiGraph()
next_queue=[ROOT_URL]
while depth<MAX_DEPTH:
        depth+=1
        (queue,next_queue)=(next_queue,[])
        for item in queue:
                try:
                        page=requests.post(item)
                except Exception:
                        print('failed to fetch'+item)
                        continue
                try:
                        soup=BeautifulSoup(page)
                except Exception:
                        print('failed to parse'+item)
                        continue

        anchorTags=soup.findAll('a')
        if not g.has_node(item):
                g.add_node(item)
        for a in anchorTags:
                if a.has_key('rel'):
                        if len(set(a['rel'].split())&XFN_TAGS)>0:
                                friend_url=a['href']
                                g.add_edge(item,friend_url)
                                g[item][friend_url]['label']=a['rel'].encode('utf-8')
                                g.node[friend_url]['label']=a.contents[0].encode('utf-8')
                                next_queue.append(friend_url)
if not os.path.iddir('out'):
        os.mkdir('out')
try:
        nx.drawing.write_dot(g,os.path.join('out',OUT))
except Exception:
        dot=[]
        for(n1,n2) in g.edges():
                dot.append('"%s" [label="%s"]' %(n2,g.node[n2]['label']))
                dot.append('""%s->"%s"[label="%s"]' %(n1,n2,g[n1][n2]['label']))
        f=open(os.path.join('out',OUT),'w')
        f.write('''strict digraph{%s}''' %(';\n'.join(dot),))
        f.close()
