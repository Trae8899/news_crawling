import json

with open("api.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

def api(site):
    id=""
    key=""
    for item in data:
        if item['SITE']==site:
            id=item['ID']
            key=item['KEY']
            return item
    
    return item