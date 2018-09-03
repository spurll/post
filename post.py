#!/usr/bin/python3

import os
import requests
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('url')
parser.add_argument(
    'data', help='Raw data to post as request body (alternatively, a file to '
    'read containing this data).'
)
parser.add_argument(
    'header', help='JSON to post as request header (alternatively, a file to '
    'read containing header JSON).', nargs='?'
)
parser.add_argument(
    '-j', '--json', help='Helpfully adds {"Content-Type": "application/json"} '
    'to the header.', action='store_true'
)
parser.add_argument(
    '-n', '--no-verify', help='Skips SSL certificate verification.',
    action='store_true'
)
args = parser.parse_args()

if os.path.isfile(args.data):
    with open(args.data) as f:
        data = f.read()
else:
    data = args.data

if args.header and os.path.isfile(args.header):
    with open(args.header) as f:
        header = json.loads(f.read())
else:
    header = json.loads(args.header) if args.header else {}

if args.json:
    header['Content-Type'] = 'application/json'

r = requests.post(
    args.url, data=data, headers=header, verify=not args.no_verify
)

if r.text:
    print('{}\n'.format(r.text))

print('Response: {}'.format(r.status_code))
