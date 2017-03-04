#! /usr/bin/python3
from lxml import html
import requests
page = requests.get('http://ugvle.ucsc.cmb.ac.lk/')
tree = html.fromstring(page.content)

postTopics = tree.xpath("//*[@class='subject' and @role='heading']/text()")
postDetails0= tree.xpath("//*[@class='posting fullpost']/text()")

postDetails=postDetails0+ tree.xpath("//*[@class='posting fullpost']/*/text()")

postDetails1=postDetails0+tree.xpath("//*[@class='posting fullpost']/*[1]/text()")
i=j=0
while i<len(postDetails) and j<len(postDetails1):
    if postDetails[i]!=postDetails1[j]:
        postDetails1[j-1]+="\n      "+postDetails[i]
        i+=1
    else:
        i+=1
        j+=1
i=0
print("")
for i in range(len(postTopics)):
    print(postTopics[i])
    print("")
    print("     ",postDetails1[i])
    print("\n\n")

