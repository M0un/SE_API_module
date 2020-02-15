import json
import requests
from google import google

misperrors = {'error': 'Error'}
mispattributes = {'input': ['url'], 'output': ['text']}
moduleinfo = {'author': 'Oun & Gindt', 'description': 'An expansion hover module to expand google search information about an URL', 'module-type': ['hover']}


def handler(q=False):
	if q is False:
		return False
	request = json.loads(q)
	if request.get('url'):
		toquery = request['url']
	else:
		misperrors['error'] = "Unsupported attributes type"
		return misperrors

	num_page = 1
	res = ""
	search_results = google.search(request['url'], num_page)
	for i in range(3):
		res += "("+str(i+1)+")" + '\t'
		res += json.dumps(search_results[i].description, ensure_ascii=False)
		res += '\n\n'
	return {'results': [{'types': mispattributes['output'], 'values':res}]}

def introspection():
	return mispattributes


def version():
	return moduleinfo
