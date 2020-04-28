import requests
from lxml import etree
URL_BASE="https://dit.gonzalonazareno.org/redmine/"
r=requests.get(URL_BASE+'projects.xml')
if r.status_code == 200:
	doc = etree.fromstring(r.text.encode('utf-8'))
	projects=doc.xpath("project/name/text()")
	for p in projects:
		print (p)
