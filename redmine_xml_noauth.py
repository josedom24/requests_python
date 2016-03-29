# -*- coding: utf-8 -*-
import requests
from lxml import etree

r=requests.get('http://dit.gonzalonazareno.org/redmine/projects.xml')
if r.status_code == 200:
	doc = etree.fromstring(r.text.encode ('utf-8'))
	projects=doc.findall("project/name")
	for p in projects:
		print p.text
