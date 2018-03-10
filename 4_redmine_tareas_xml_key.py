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
	projects=doc.findall("project")
	for p in projects:
		if p.find("name").text==proyecto: 
			id_project=p.find("id").text


payload = {'status_id':'open','limit':'5','project_id':id_project,'key':key}
r=requests.get('http://dit.gonzalonazareno.org/redmine/issues.xml',params=payload)
if r.status_code == 200:
	doc = etree.fromstring(r.text.encode ('utf-8'))
	tareas=doc.findall("issue")
	for t in tareas:
		print (t.find("assigned_to").attrib["name"])
		print (t.find("subject").text)
else:
	print ("Error de proyecto")