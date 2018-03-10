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
	projects=doc.findall("project/name")
	ids=doc.findall("project/id")
	encontrado=False
	for p,id in zip(projects,ids):
		if p.text==proyecto:
			encontrado=True
			payload["limit"]=5
			payload["project_id"]=id.text
			r=requests.get(URL_BASE+'/issues.xml',params=payload)
			if r.status_code==200:
				doc = etree.fromstring(r.text.encode ('utf-8'))
				names=doc.findall("issue/subject")
				descriptions=doc.findall("issue/description")	
				for name,desc in zip(names,descriptions):
					print (name.text)
					print (desc.text)

	if not encontrado:
		print ("Proyecto no existe")