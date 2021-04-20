# -*- coding: utf-8 -*-

import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

url = "https://www.newegg.com/p/pl?Submit=ENE&N=100007709%2050001312%2050001314%2050001315%2050001402%2050001419%2050001471%2050001561%2050001944%2050012150%204814%20601201888%20601204369%20601301599%20601296379%20601296377%2050001669%20601321570%20601321572%20601323902%20601328427%20601331000%20601331379%20600419577%20600536666%20601341679&IsNodeId=1&cm_sp=Cat_video-Cards_1-_-Visnav-_-Gaming-Video-Cards_1"

# opening connection, grabbing page
client = ureq(url)

# puts html into variable
html = client.read()

client.close()

# html parsing
page_soup = soup(html, "html.parser")

containers = page_soup.findAll("div",{"class":"item-container"})

filename = "products.csv"
f = open(filename,'w')

headers = "brand, name, price, shipping\n"
f.write(headers)

for c in containers:
    info = c.find("div","item-info")
    brand = info.div.a.img["title"]
    name = info.find("a","item-title").text
    price = info.find("li","price-current").strong.text
    shipping = info.find("li","price-ship").text.strip()
    
    f.write(brand + "," + name.replace(",","|") + "," + price.replace(",","") + "," + shipping + "\n")
    
f.close()

