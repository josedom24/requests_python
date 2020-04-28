import requests
import os
from lxml import etree
URL_BASE="https://dit.gonzalonazareno.org/redmine/"
key=os.environ["key"]
payload = {'key':key}


r=requests.get(URL_BASE+'projects.xml',params=payload)
if r.status_code == 200:
	doc = etree.fromstring(r.text.encode ('utf-8'))
	projects=doc.xpath("project")
	for p in projects:
		if p.xpath("name/text()")[0]=="test project": 
			id_project=p.xpath("id/text()")[0]



r = requests.delete(URL_BASE+'projects/%s.xml'%id_project, params=payload)


if r.status_code==200:
 	print ("ok")
else:
 	print ("Error: "+r.text)
	


