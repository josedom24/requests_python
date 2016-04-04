# -*- coding: utf-8 -*-
import requests
from lxml import etree

ciudad = raw_input("Ciudad:")
payload = {'q': ciudad, 'mode': 'xml','units':'metric','APPID':'224045b10874d0e48810401aa1455c4e'}
r=requests.get('http://api.openweathermap.org/data/2.5/weather',params=payload)
if r.status_code == 200:
	doc = etree.fromstring(r.text.encode ('utf-8'))
	temp=doc.find("temperature").attrib["value"]
	print temp+" ºC"


