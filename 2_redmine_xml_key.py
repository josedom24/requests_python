# -*- coding: utf-8 -*-
import requests
from lxml import etree

payload = {'key':'466f4055fe2f206676793d544b06ddee64b45432'}
r=requests.get('http://dit.gonzalonazareno.org/redmine/projects.xml',params=payload)
if r.status_code == 200:
	doc = etree.fromstring(r.text.encode ('utf-8'))
	projects=doc.findall("project/name")
	for p in projects:
		print p.text
	
