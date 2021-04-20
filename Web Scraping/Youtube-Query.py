# -*- coding: utf-8 -*-

import re
import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

url = "https://www.youtube.com/results?search_query=cat"

# opening connection, grabbing page
client = ureq(url)

# puts html into variable
html = client.read()

# html parsing
page_soup = soup(html, "html.parser")

view = page_soup.findAll("ul",{"class":"yt-lockup-meta-info"})

title = page_soup.findAll("h3", {"class":"yt-lockup-title"})
titles = []
for i in title:
    titles.append(i.a.text)
    
byline = page_soup.findAll("div",{"class":"yt-lockup-byline"})
bylines = []
for i in byline:
    bylines.append(i.a.text)

meta = page_soup.findAll("ul",{"class":"yt-lockup-meta-info"})
views = []
dates = []

for i in meta:
    if (len(i.findAll("li")) == 1):
        number = i.findAll("li")[0].text
        s = re.search('\d+.+(?=\s)', number)
        number = s.group(0)
        views.append(number)
        dates.append("N/A")
    else:
        number = i.findAll("li")[1].text
        s = re.search('\d+.+(?=\s)', number)
        number = s.group(0)
        views.append(number)
        dates.append(i.findAll("li")[0].text)

mapped = zip(titles, bylines, views, dates)
mapped = set(mapped)

for i in mapped:
    print(i[0], " | ", i[2], " | ", i[3])



