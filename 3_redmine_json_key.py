# -*- coding: utf-8 -*-
import requests
payload = {'key':'466f4055fe2f206676793d544b06ddee64b45432'}
r=requests.get('http://dit.gonzalonazareno.org/redmine/projects.json',params=payload)
if r.status_code == 200:
	doc=r.json()
	for p in doc["projects"]:
		print str(p["id"])+" - "+p["name"]
	

