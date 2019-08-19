#!/usr/bin/python3

import os
import requests
import argparse
import json

parser = argparse.ArgumentParser()

parser.add_argument('url')
parser.add_argument(
    'data', help='Raw data to post as request body (alternatively, a file to '
    'read containing this data).', nargs='?'
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

type = parser.add_mutually_exclusive_group()
type.add_argument(
    '-p', '--put', help='Issue PUT request instead of POST.',
    action='store_true'
)
type.add_argument(
    '-g', '--get', help='Issue GET request instead of POST (payload is '
    'ignored).', action='store_true'
)
type.add_argument(
    '-d', '--delete', help='Issue DELETE request instead of POST (payload is '
    'ignored).', action='store_true'
)
type.add_argument(
    '-e', '--head', help='Issue HEAD request instead of POST (payload is '
    'ignored).', action='store_true'
)
type.add_argument(
    '-o', '--options', help='Issue OPTIONS request instead of POST (payload '
    'is ignored).', action='store_true'
)

args = parser.parse_args()

if args.data and os.path.isfile(args.data):
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

request = requests.put if args.put \
    else requests.get if args.get \
    else requests.head if args.head \
    else requests.options if args.options \
    else requests.post

if request == requests.put or request == requests.post:
    r = request(args.url, data=data, headers=header, verify=not args.no_verify)
else:
    r = request(args.url, headers=header, verify=not args.no_verify)

if r.text:
    print('{}\n'.format(r.text))

print('Response: {}'.format(r.status_code))
