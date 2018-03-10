import requests
from lxml import etree
key=os.environ["key"]
payload = {'key':key}


r=requests.get('http://dit.gonzalonazareno.org/redmine/projects.xml',params=payload)
if r.status_code == 200:
	doc = etree.fromstring(r.text.encode ('utf-8'))
	projects=doc.findall("project")
	for p in projects:
		if p.find("name").text=="test project": 
			id_project=p.find("id").text



r = requests.delete('http://dit.gonzalonazareno.org/redmine/projects/%s.xml'%id_project, params=payload)


if r.status_code==200:
 	print ("ok")
 else:
 	print ("Error: "+r.text)
	


