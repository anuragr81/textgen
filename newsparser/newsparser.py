#!/usr/bin/python3.3


import requests
import datetime,re
import pprint

import xml.etree.ElementTree as ET
strURL  = 'http://feeds.reuters.com/reuters/UKPersonalFinanceNews'
outFile = 't.html'


dat = []

r = requests.get(strURL)

with open(outFile,'wb') as fh:
          fh.write(r.text.encode())

root = ET.parse(outFile).getroot()
for elem in root.find('channel'):
   if (elem.tag == "lastBuildDate"):
      dat.append({str(elem.text):{}})

   if (elem.tag=="item"):
      for pubDate in elem.findall("pubDate"):
          pubTime=datetime.datetime.strptime(pubDate.text, "%a, %d %b %Y %H:%M:%S %z")
          dat[-1][pubTime]={}
          for subElem in elem.findall("title"):               
              dat[-1][pubTime]['title']=subElem.text
          for subElem in elem.findall("description"):             
              dat[-1][pubTime]['description']=re.search("(.*)<div",subElem.text).group(1)
                                                                                                                                       
                                                                                                                                       
                                                                                                                                       
print(dat)
