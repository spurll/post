# post

Python command-line utility that issues HTTP POST commands.

# Usage

```
./post.py [-h] url data [header]
```

* `url`: the URL
* `data`: either raw data to post as the request body or the path to a file to read
  containing this data
* `header` (optional): either JSON to post as the request header or the path to a file
  to read containing header JSON

The response code and anything else returned by the server will be sent to the console.

## Optional Flags

* `-j`/`--json`: Helpfully adds `{"Content-Type": "application/json"}` to the header
* `-n`/`--no-verify`: Skips SSL certificate verification

## Setup

You'll need to install `requests`.

# Examples

```sh
$ ./post.py https://example.com/real_endpoint test.json
Response: 200
```

```sh
$ ./post.py https://example.com/fake_endpoint test.json
Response: 404
```

```sh
$ ./post.py https://example.com/reset-password '{"username": "your.email@example.com"}' -j
Response: 204
```

The last example above is equivalent to:

```sh
$ ./post.py https://example.com/reset-password '{"username": "your.email@example.com"}' '{"Content-Type": "application/json"}'
Response: 204
```

# License Information

Written by Gem Newman. [Website](http://spurll.com) | [GitHub](https://github.com/spurll/) | [Twitter](https://twitter.com/spurll)

This work is licensed under the [Mozilla Public License 2.0](https://www.mozilla.org/en-US/MPL/2.0/).

Remember: [GitHub is not my CV](https://blog.jcoglan.com/2013/11/15/why-github-is-not-your-cv/).
