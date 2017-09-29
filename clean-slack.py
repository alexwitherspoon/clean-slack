import urllib
import urllib2
import time
import json


# load the configuration file
with open('clean-slack.conf', 'r') as f:
    config = json.load(f)

token = config['DEFAULT']['TOKEN'] # API Token for Slack
days = config['DEFAULT']['DAYS'] # delete files older than this


ts_to = int(time.time()) - days * 24 * 60 * 60

# find list of channels
def list_channels():
  params = {
    'token': token
  }
  uri = 'https://slack.com/api/channels.list'
  response = urllib2.urlopen(uri + '?' + urllib.urlencode(params)).read()
  return json.loads(response)['channels']

# find list of messages in channels
def list_messages(channel_ids):
  for channel_id in channel_ids:
    params = {
      'token': token,
      'channel': channel_id,
      'latest': ts_to,
      'oldest': 1
    }
    uri = 'https://slack.com/api/channels.history'
    response = urllib2.urlopen(uri + '?' + urllib.urlencode(params)).read()
    messages = json.loads(response)['messages']
    messages_ids = [f['ts'] for f in messages]
    for message_id in messages_ids:
        #print channel_id, messages_id
        delete_messages(channel_id, message_id) 

# delete messages that match criterea
#TODO
def delete_messages(channel_id, message_id):
  params = {
    'token': token,
    'channel': channel_id,
    'ts': message_id
  }
  uri = 'https://slack.com/api/chat.delete'
  response = urllib2.urlopen(uri + '?' + urllib.urlencode(params)).read()
  print channel_id, message_id, json.loads(response)['ok']

# find list of files
def list_files():
  params = {
    'token': token,
    'ts_to': ts_to,
    'count': 1000
  }
  uri = 'https://slack.com/api/files.list'
  response = urllib2.urlopen(uri + '?' + urllib.urlencode(params)).read()
  print json.loads(response)['files']
  return json.loads(response)['files']

# delete files that match criterea
def delete_files(file_ids):
  count = 0
  num_files = len(file_ids)
  for file_id in file_ids:
    count = count + 1
    params = {
      'token': token,
      'file': file_id
      }
    uri = 'https://slack.com/api/files.delete'
    response = urllib2.urlopen(uri + '?' + urllib.urlencode(params)).read()
    print count, "of", num_files, "-", file_id, json.loads(response)['ok']

# manage Messages
# TODO
channels = list_channels()
channel_ids = [f['id'] for f in channels]
list_messages(channel_ids)

# Manage Files
files = list_files()
file_ids = [f['id'] for f in files]
delete_files(file_ids)
