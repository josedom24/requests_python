import requests
from lxml import etree
import os
key=os.environ["key"]


proyecto=input("Dime el nombre de un proyecto:")
id_project=""

payload = {'key':key}
r=requests.get('http://dit.gonzalonazareno.org/redmine/projects.xml',params=payload)
if r.status_code == 200:
	doc = etree.fromstring(r.text.encode ('utf-8'))
	projects=doc.xpath("project")
	for p in projects:
		if p.xpath("name/text()")[0]==proyecto: 
			id_project=p.xpath("id/text()")[0]


payload = {'status_id':'open','limit':'5','project_id':id_project,'key':key}
r=requests.get('http://dit.gonzalonazareno.org/redmine/issues.xml',params=payload)
if r.status_code == 200:
	doc = etree.fromstring(r.text.encode ('utf-8'))
	tareas=doc.xpath("issue")
	for t in tareas:
		print (t.xpath("assigned_to/@name")[0])
		print (t.xpath("subject/text()")[0])
else:
	print ("Error de proyecto")