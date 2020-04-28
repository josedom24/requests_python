import requests
import os
URL_BASE="https://dit.gonzalonazareno.org/redmine/"
key=os.environ["key"]
payload = {'key':key}
r=requests.get(URL_BASE+'projects.json',params=payload)
if r.status_code == 200:
	doc=r.json()
	for p in doc["projects"]:
		print (str(p["id"])+" - "+p["name"])
	

