import requests

url = 'http://127.0.0.1:8080/api/v2/users/'
headers = {'content-type': 'application/json',
           'Authorization': 'Token b5ecc643f369e14f105778e1b005a07d75a88da9'}
r = requests.get(url, headers=headers, verify=True) # set verify to False if ssl cert is self-signed

for key, value in r.__dict__.iteritems():
  print(key)
  print(value)
  print('------------------')
