import json
import re

with open('AllCards.json') as json_file:
    data = json.load(json_file)

    dragonKeys = []

    for key in data.keys():
        if (re.match(r'[Dd]ragon', key)):
            dragonKeys.append(key)

    for key in dragonKeys:
        print key + ' ' + str(data[key]['colors'])

    # theKey = data.keys()[0]
    # theRecord = data[theKey]

    # print theKey
    # print theRecord['colors']