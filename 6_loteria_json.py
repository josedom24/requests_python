import requests
import json
numero=input("Dame el número:")
payload = {'n':numero}
r=requests.get('http://api.elpais.com/ws/LoteriaNavidadPremiados',params=payload)
if r.status_code == 200:
	doc=r.text.split("=")[1]
	js=json.loads(doc)
	print (js["premio"])
	

