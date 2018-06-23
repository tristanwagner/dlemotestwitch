import urllib
import os
import json

if not os.path.exists('./emotes'):
    os.makedirs('./emotes')
print('Saving emotes to folder: ' + os.path.abspath('./emotes'))
print('Grabbing emote list...')
emotes = json.load(urllib.urlopen('https://twitchemotes.com/api_cache/v3/global.json'))
for code, emote in emotes.items():
    print('Downloading: ' + code + '...')
    url = 'https://static-cdn.jtvnw.net/emoticons/v1/' + str(emote['id']) + '/1.0'
    print url
    filepath = './emotes/' + code + '.png'
    urllib.urlretrieve(url,
                       filepath)

print('Done')
