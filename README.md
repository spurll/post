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

```sh
$ ./post.py http://example.com/real_endpoint test.json
Response: 200
```

```sh
$ ./post.py http://example.com/fake_endpoint test.json
Response: 404
```

# License Information

Written by Gem Newman. [Website](http://spurll.com) | [GitHub](https://github.com/spurll/) | [Twitter](https://twitter.com/spurll)

This work is licensed under the [Mozilla Public License 2.0](https://www.mozilla.org/en-US/MPL/2.0/).

Remember: [GitHub is not my CV](https://blog.jcoglan.com/2013/11/15/why-github-is-not-your-cv/).
