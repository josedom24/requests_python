import requests
import os
URL_BASE="https://dit.gonzalonazareno.org/redmine/"

key=os.environ["key"]
payload = {'key':key}


xml_project="""
<project>
	<name>test project</name>
	<identifier>test1</identifier>
	<enabled_module_names>time_tracking</enabled_module_names>
	<enabled_module_names>issue_tracking</enabled_module_names>
</project>
"""


headers = {'Content-Type': 'application/xml'}
r = requests.post(URL_BASE+'projects.xml', params=payload, data=xml_project, headers=headers)
if r.status_code==201:
	print ("ok")
else:
	print ("Error: "+r.text)
	