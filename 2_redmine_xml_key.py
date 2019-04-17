import requests
from lxml import etree
import os
key=os.environ["key"]
payload = {'key':key}
r=requests.get('http://dit.gonzalonazareno.org/redmine/projects.xml',params=payload)
if r.status_code == 200:
	doc = etree.fromstring(r.text.encode ('utf-8'))
	projects=doc.xpath("project/name")
	for p in projects:
		print (p.text)
	
