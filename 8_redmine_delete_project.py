import requests
from lxml import etree
key=os.environ["key"]
payload = {'key':key}


r=requests.get('http://dit.gonzalonazareno.org/redmine/projects.xml',params=payload)
if r.status_code == 200:
	doc = etree.fromstring(r.text.encode ('utf-8'))
	projects=doc.xpath("project")
	for p in projects:
		if p.xpath("name/text()")[0]=="test project": 
			id_project=p.xpath("id/text()")[0]



r = requests.delete('http://dit.gonzalonazareno.org/redmine/projects/%s.xml'%id_project, params=payload)


if r.status_code==200:
 	print ("ok")
 else:
 	print ("Error: "+r.text)
	


