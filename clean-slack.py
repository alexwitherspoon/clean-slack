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

# find list of files
def list_files():
  params = {
    'token': token,
    'ts_to': ts_to,
    'count': 1000,
  }
  uri = 'https://slack.com/api/files.list'
  response = urllib2.urlopen(uri + '?' + urllib.urlencode(params)).read()
  return json.loads(response)['files']

# delete files that match criterea
def delete_files(file_ids):
  count = 0
  num_files = len(file_ids)
  for file_id in file_ids:
    count = count + 1
    params = {
      'token': token
      ,'file': file_id
      }
    uri = 'https://slack.com/api/files.delete'
    response = urllib2.urlopen(uri + '?' + urllib.urlencode(params)).read()
    print count, "of", num_files, "-", file_id, json.loads(response)['ok']

files = list_files()
file_ids = [f['id'] for f in files]
delete_files(file_ids)
