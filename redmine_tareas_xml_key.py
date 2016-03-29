# -*- coding: utf-8 -*-
import requests
from lxml import etree
import os

payload = {'limit':'100','id':'24','key':os.environ['key']}
r=requests.get('http://dit.gonzalonazareno.org/redmine/issues.xml',params=payload)
if r.status_code == 200:
	doc = etree.fromstring(r.text.encode ('utf-8'))
	tareas=doc.findall("issue")
	for t in tareas:
		print t.find("assigned_to").attrib["name"]
		print t.find("subject").text
