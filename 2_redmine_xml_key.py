import requests
from lxml import etree
import os
URL_BASE="https://dit.gonzalonazareno.org/redmine/"
key=os.environ["key"]
payload = {'key':key}
r=requests.get(URL_BASE+'projects.xml',params=payload)
if r.status_code == 200:
	doc = etree.fromstring(r.text.encode ('utf-8'))
	projects=doc.xpath("project/name/text()")
	for p in projects:
		print (p)
	
