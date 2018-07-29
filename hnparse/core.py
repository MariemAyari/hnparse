#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This module extract posts from hacker news."""
import requests
import bs4


def extract(page, post_count):
    """Parses hacker news posts and returns set of dictionaries each containing:
         * title: The title of the post
         * rank: Post rank in hacker news
         * uri: uri of the post
         * score: Post score if defined otherwise 0
         * author: Name of the post author. If not mentioned defaults to 'Not defined'
         * comments: Number of post's comments. Defaults to 0 if no comment found

     keyword arguments:
     page -- page from which to extract nb_posts
     post_count -- number of posts to extract from the page
     """
    posts=[]
    uri="https://news.ycombinator.com/news?p={}".format(page)
    res=requests.get(uri)
    soup=bs4.BeautifulSoup(res.text,'lxml')
    tab=soup.select('.itemlist')[0]
    for i in tab.select('.athing')[0:post_count]:
         item={}
         item['title']=i.select('.storylink')[0].text
         item['uri']=i.select('.storylink')[0]['href']
         item['rank']= int(i.select('.rank')[0].text[0:-1])
         posts.append(item)
    for idx,j in enumerate(tab.select('.subtext')[0:post_count]):
         posts[idx]['score']=int(j.select('.score')[0].text.split(" ")[0]) if len(j.select('.score'))>0 else 0
         posts[idx]['author']=j.select('.hnuser')[0].text if len(j.select('.hnuser'))>0 else 'Not defined'
         links=j.find_all('a')
         if len(links) == 4 and 'discuss' not in links[3]:
            posts[idx]['comments']=int(links[3].text.split(u"\u00A0")[0])
         else:
            posts[idx]['comments']=0
    return posts
