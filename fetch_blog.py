import json
import requests
import dateutil.parser

try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

content = requests.get("https://bits.mdminhazulhaque.io/feed.xml").text
soup = BeautifulSoup(content, "lxml")
entries = soup.find_all("entry")

data = []

for entry in entries[:4]:
    link = entry.link['href']
    
    blog = {
        "url_title": link,
        "title": entry.title.text,
        "sub_title": entry.summary.text,
        "date": dateutil.parser.isoparse(entry.published.text).strftime("%d %b %Y"),
        "tag": link.split("/")[3],
        "visible": True
    }
    
    data.append(blog)

with open("data/blog.json", "w") as fp:
    json.dump(data, fp, indent=4)
