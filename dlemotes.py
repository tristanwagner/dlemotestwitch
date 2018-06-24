import urllib
import os
import json

if not os.path.exists('./emotes'):
    os.makedirs('./emotes')

print('Saving emotes to folder: ' + os.path.abspath('./emotes'))
print('Grabbing emote list...')

if not os.path.exists('./emotes/global'):
    os.makedirs('./emotes/global')

emotesglobal = json.load(urllib.urlopen('https://twitchemotes.com/api_cache/v3/global.json'))
for code, emote in emotesglobal.items():
    print('Downloading: ' + code + '...')
    url = 'https://static-cdn.jtvnw.net/emoticons/v1/' + str(emote['id']) + '/1.0'
    print url
    filepath = './emotes/global/' + code + '.png'
    urllib.urlretrieve(url,
                       filepath)

if not os.path.exists('./emotes/subs'):
    os.makedirs('./emotes/subs')

emotessubs = json.load(urllib.urlopen('https://twitchemotes.com/api_cache/v3/subscriber.json'))

for id, data in emotessubs.items():
    print('Channel : ' + data['channel_name'])
    for emote in data['emotes']:
        print('Downloading: ' + emote['code'] + '...')
        url = 'https://static-cdn.jtvnw.net/emoticons/v1/' + str(emote['id']) + '/1.0'
        print url
        filepath = './emotes/subs/' + data['channel_name'] + '/' + emote['code'] + '.png'
        if not os.path.exists('./emotes/subs/' + data['channel_name']):
            os.makedirs('./emotes/subs/' + data['channel_name'])
        urllib.urlretrieve(url,
                           filepath)

print('Done')
