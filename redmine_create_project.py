import requests

payload = {'key':'466f4055fe2f206676793d544b06ddee64b45432'}


xml_project="""
<project>
	<name>test project</name>
	<identifier>test</identifier>
	<enabled_module_names>time_tracking</enabled_module_names>
	<enabled_module_names>issue_tracking</enabled_module_names>
</project>
"""



r=requests.post('http://dit.gonzalonazareno.org/redmine/projects.xml',data={'project':xml_project,'key':payload["key"]})
print r.body	
print r.status_code
if r.status_code == 201:
	print "ok"
	