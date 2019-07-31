import json

with open('AllCards.json') as json_file:
    data = json.load(json_file)
    theKey = data.keys()[0]
    theRecord = data[theKey]

    print theKey
    print theRecord['colors']