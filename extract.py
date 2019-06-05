import json
import sys

import requests
import lxml.html

url = "https://songwhip.com/"

querystring = {"utm_source":"songwhip-home-paste"}

payload = sys.argv[1]
headers = {
    'origin': "https://songwhip.com",
    'accept-language': "en-US,en;q=0.9",
    'cookie': "__cfduid=de68de6f9e9fc6fc795e27a5e8c4a7c9d1559767541",
    'pragma': "no-cache",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36",
    'content-type': "application/json",
    'accept': "*/*",
    'cache-control': "no-cache,no-cache",
    'authority': "songwhip.com",
    'referer': "https://songwhip.com/",
    'dnt': "1",
    'Postman-Token': "37c18515-02d5-4763-90c2-43684ec0aa26"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

links_page = requests.request("GET", response.json()['url'])
doc = lxml.html.fromstring(links_page.content)


things = doc.xpath('//*[@id="main"]/div/div/div[1]/div[2]/div/div/ul/li')

link_dict = {thing.xpath('.//a')[0].text: thing.xpath('.//a')[0].get('href') for thing in things}

data = {"items":
    [
	{
		"uid": "desktop",
		"title": source,
		"arg": link,
		"autocomplete": "Desktop",
		"icon": {
			"type": "fileicon",
			"path": "~/Desktop"
		}
	} for source, link in link_dict.items()
]
}

sys.stdout.write(json.dumps(data))