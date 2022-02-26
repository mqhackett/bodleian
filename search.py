'''
This file scrapes the stolostron organization for all yaml files
ORG is the github.com org that we are scraping
'''

import requests
import base64


ORG="stolostron"

# gets the full response object. All yaml files in stolostron
# TODO: get the paginated version of the queries. Pretty sure you have to do pages
#       totol count reads 5k but items list reads 30 
def get_yamls():
	headers = {'Accept': 'application/vnd.github.v3+json'}
	url = 'https://api.github.com/search/code?q=language:yaml+org:'+ORG
	r = requests.get(url, headers=headers)
	res = r.json()
	print len(res)
	return res


# returns a list of the yaml names
def get_names(yamls):
	for i in yamls['items']:
		print i['name']
	
# given a yaml response object from github, output the raw yaml
def get_raw_yaml(yaml):
	url = yaml['url']	
	r = requests.get(url)
	res = r.json()
	content = res['content']
	raw_yaml = base64.b64decode(content)
	return raw_yaml




def main():
	yamls = get_yamls()
	print len(yamls['items'])
	
	first_yaml = yamls['items'][0]
	print first_yaml['name'], get_raw_yaml(first_yaml)
	

if __name__ == "__main__":
	main()
