import requests
from settings import get

base_url = 'http://localhost:3000'

pload = {'email': get('receiver_email'), 'password': get('password')}
r = requests.post(base_url + '/auth/sign_in', data = pload)

access_token = r.headers['access-token']
client = r.headers['client']
uid = r.headers['uid']

pload = {'access-token': access_token, 'client': client, 'uid': uid}

response = requests.get('http://localhost:3000/tickers', data=pload).json()

