import requests
from lxml import etree
import os
key=os.environ["key"]
ciudad = input("Ciudad:")
payload = {'q': ciudad, 'mode': 'xml','units':'metric','APPID':key}
r=requests.get('http://api.openweathermap.org/data/2.5/weather',params=payload)
if r.status_code == 200:
	doc = etree.fromstring(r.text.encode ('utf-8'))
	temp=doc.find("temperature").attrib["value"]
	print (temp+" ºC")


