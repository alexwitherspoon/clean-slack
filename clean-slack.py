import urllib
import urllib2
import time
import json

token = ''

#Delete files older than this:
days = 60
ts_to = int(time.time()) - days * 24 * 60 * 60

def list_files():
  params = {
    'token': token,
    'ts_to': ts_to,
    'count': 1000,
  }
  uri = 'https://slack.com/api/files.list'
  response = urllib2.urlopen(uri + '?' + urllib.urlencode(params)).read()
  return json.loads(response)['files']

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
