import requests
from lxml import etree
import os
key=os.environ["key"]
URL_BASE="http://dit.gonzalonazareno.org/redmine"
payload={"key":key}
proyecto=input("Proyecto:")
r=requests.get(URL_BASE+'/projects.xml',params=payload)
if r.status_code == 200:
	doc = etree.fromstring(r.text.encode ('utf-8'))
	projects=doc.xpath("project/name/text()")
	ids=doc.xpath("project/id/text()")
	encontrado=False
	for p,id in zip(projects,ids):
		if p==proyecto:
			encontrado=True
			payload["limit"]=5
			payload["project_id"]=id
			r=requests.get(URL_BASE+'/issues.xml',params=payload)
			if r.status_code==200:
				doc = etree.fromstring(r.text.encode ('utf-8'))
				names=doc.xpath("issue/subject")
				descriptions=doc.xpath("issue/description")	
				for name,desc in zip(names,descriptions):
					print (name.text)
					print (desc.text)

	if not encontrado:
		print ("Proyecto no existe")