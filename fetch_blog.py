import xmltodict
import json
import requests

xmldata = requests.get("https://bits.mdminhazulhaque.io/feed.xml").text
jsondata = xmltodict.parse(xmldata)

data = []

for entry in jsondata['feed']['entry'][:4]:
    blog = {
        "url_title": entry['link']['@href'],
        "title": entry['title']['#text'],
        "sub_title": entry['summary']['#text'],
        "date": entry['published'][:10],
        "tag": entry['link']['@href'].split("/")[3],
        "visible": True
    }
    data.append(blog)

with open("data/blog.json", "w") as fp:
    json.dump(data, fp, indent=4)
