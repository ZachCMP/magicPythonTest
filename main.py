import json

with open('/test thing/AllCards.json') as json_file:
    data = json.load(json_file)
    print len(data.keys())