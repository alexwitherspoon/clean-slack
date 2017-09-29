import urllib
import urllib2
import time
import json


# load the configuration file
with open('clean-slack-channel.conf', 'r') as f:
    config = json.load(f)

token = config['DEFAULT']['TOKEN'] # API Token for Slack
days = config['DEFAULT']['DAYS'] # delete items older than this
channel = config['DEFAULT']['CHANNEL'] # Delete messages from this channel


ts_to = int(time.time()) - days * 24 * 60 * 60

# find list of messages in channels
def list_messages(channel):
  params = {
    'token': token,
    'channel': channel_id,
    'latest': ts_to,
    'oldest': 1
  }
  uri = 'https://slack.com/api/channels.history'
  response = urllib2.urlopen(uri + '?' + urllib.urlencode(params)).read()
  print response
  print 'ECHO'
  print json.loads(response)['messages']
  messages = json.loads(response)['messages']
  messages_ids = [f['ts'] for f in messages]
  for message_id in messages_ids:
    delete_messages(channel_id, message_id) 

# delete messages that match criterea
def delete_messages(channel_id, message_id):
  time.sleep(1)
  params = {
    'token': token,
    'channel': channel_id,
    'ts': message_id
  }
  uri = 'https://slack.com/api/chat.delete'
  response = urllib2.urlopen(uri + '?' + urllib.urlencode(params)).read()
  print 'Deleting', channel_id, message_id, json.loads(response)['ok']

# manage Messages
list_messages(channel)
