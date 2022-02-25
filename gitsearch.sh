# We'll use the `date` command to get the date for "7 days ago"
date -v-7d '+%Y-%m-%d'
# => 2013-07-15

curl -G https://api.github.com/search/repositories       \
  --data-urlencode "q=created:>`date -v-7d '+%Y-%m-%d'`" \
  --data-urlencode "sort=stars"                          \
  --data-urlencode "order=desc"                          \
  -H "Accept: application/vnd.github.preview"            \
  | jq ".items[0,1,2] | {name, description, language, watchers_count, html_url}"
