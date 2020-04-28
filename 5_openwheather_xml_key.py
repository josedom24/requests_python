import requests
from lxml import etree
import os
URL_BASE="https://api.openweathermap.org/data/2.5/"
key=os.environ["key"]
ciudad = input("Ciudad:")
payload = {'q': ciudad, 'mode': 'xml','units':'metric','APPID':key}
r=requests.get(URL_BASE+'weather',params=payload)
if r.status_code == 200:
	doc = etree.fromstring(r.text.encode ('utf-8'))
	temp=doc.xpath("temperature/@value")[0]
	print (temp+" ºC")


