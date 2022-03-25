# gets all the open PRs for the projects listed in the projects array


for i in $(cat repos); do 
    url="https://api.github.com/repos/stolostron/"$i"/pulls"
    curl -s -G $url -H "Accept: application/vnd.github.preview" | jq ".[] | {html_url, title}"| jq '.title, .html_url' 
	done;

# curl -s -G $url -H "Accept: application/vnd.github.preview" |\
#     jq ".[] | {html_url, title, users}"| jq '.title, .html_url, .users' 

# curl -G https://api.github.com/repos/stolostron/search-collector/pulls       \
#   --data-urlencode "state=open" \
#   -H "Accept: application/vnd.github.preview"            \
#   | jq ".[] | {html_url, title}"





