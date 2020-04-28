import requests
URL_BASE="https://swapi.dev/api/"
r=requests.get(URL_BASE+'people/')
if r.status_code == 200:
	doc = r.json()
	print("Número de ersonajes:",doc["count"])
	for resultado in doc["results"]:
		print(resultado["name"])
	pagina=2
	tecla=input("Pulsa espacio para continuar o otra tecla para salir...")
	while doc["next"]!=None and tecla==" ":
		payload={"page":pagina}
		r=requests.get(URL_BASE+'planets/',params=payload)
		if r.status_code == 200:
			doc = r.json()
			for resultado in doc["results"]:
				print(resultado["name"])
			pagina=pagina+1
			tecla=input("Pulsa espacio para continuar o otra tecla para salir...")
else:
	print("Error en la API")



nombre=input("Dime el nombre de un personaje:")
payload={"search":nombre}
r=requests.get(URL_BASE+'people/',params=payload)
if r.status_code == 200:
	doc = r.json()
	if doc["count"]==0:
		print("Personaje no encontrado")
	else:
	
		print("Altura:",doc["results"][0]["height"])
		print("Peso:",doc["results"][0]["mass"])
		print("Color del pelo:",doc["results"][0]["hair_color"])
		print("Color del piel:",doc["results"][0]["skin_color"])
		print("Color de los ojos:",doc["results"][0]["eye_color"])
		print("Año de nacimiento:",doc["results"][0]["birth_year"])
		r=requests.get(doc["results"][0]["species"][0])
		if r.status_code == 200:
			doc = r.json()
			print("Especie:",doc["name"])
			

else:
	print("Error en la API")