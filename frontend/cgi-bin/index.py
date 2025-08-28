#! /usr/bin/env python3
import cgi
import cgitb
import json
import os
from urllib import request

cgitb.enable()

BACKEND_URL = os.environ.get('BACKEND_URL', 'http://127.0.0.1:8080')

form = cgi.FieldStorage()
action = form.getfirst('action', 'health')

print('Content-Type: application/json\r\n\r\n', end='')

try:
	if action == 'fetch_alerts':
		with request.urlopen(f'{BACKEND_URL}/alerts/fetch', timeout=5) as resp:
			data = resp.read().decode('utf-8')
			print(data)
	else:
		with request.urlopen(f'{BACKEND_URL}/health', timeout=5) as resp:
			data = resp.read().decode('utf-8')
			print(data)
except Exception as exc:
	print(json.dumps({'error': str(exc)}))
