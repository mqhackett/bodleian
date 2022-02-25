import requests
import base64


# gets the full response object. All yaml files in stolostron
def get_yaml():
	headers = {'Accept': 'application/vnd.github.v3+json'}
	url = 'https://api.github.com/search/code?q=language:yaml+org:stolostron'
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
	yamls = get_yaml()
	print len(yamls['items'])
	
	first_yaml = yamls['items'][0]
	print first_yaml['name'], get_raw_yaml(first_yaml)
	

if __name__ == "__main__":
	main()
