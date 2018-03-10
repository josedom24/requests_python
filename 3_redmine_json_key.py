import requests
import os
key=os.environ["key"]
payload = {'key':key}
r=requests.get('http://dit.gonzalonazareno.org/redmine/projects.json',params=payload)
if r.status_code == 200:
	doc=r.json()
	for p in doc["projects"]:
		print (str(p["id"])+" - "+p["name"])
	

