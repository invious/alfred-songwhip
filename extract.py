import json
import sys

import requests
import lxml.html

url = "https://songwhip.com/"

payload = sys.argv[1]

response = requests.request("POST", url, data=payload)

links_page = requests.request("GET", response.json()['url'])
doc = lxml.html.fromstring(links_page.content)

elements = doc.xpath("//div/a[contains(@href,'http')][not(contains(@href,'songwhip'))]")
link_dict = {el.xpath("div[contains(@class,'regular')]")[0].text: el.get('href') for el in elements}

data = {"items":
    [
        {
            "uid": "desktop",
            "title": source,
            "arg": "copy",
            "mods": {
                "cmd": {
                    "valid": True,
                    "arg": "go",
                    "subtitle": "Visit Link"
                }
            },
            "autocomplete": source,
            "icon": {
                "type": "fileicon",
                "path": "./icons/" + source + '.png'
            },
            "variables": {
                "url": link,
            }

        } for source, link in link_dict.items()
    ]
}

sys.stdout.write(json.dumps(data))
