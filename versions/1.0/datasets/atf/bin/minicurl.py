#!/usr/bin/python

import sys
import urlparse
import os
import requests


def chunkedFetchUrl(url, local_filename=None, **kwargs):
    """Adapted from http://stackoverflow.com/q/16694907"""
    if not local_filename:
        local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True, **kwargs)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
    return local_filename

url=sys.argv[1]
parsed=urlparse.urlparse(url)
(h,t) = os.path.split(parsed.path)
t = t or 'index.html'
bits = parsed.netloc.split('.')
if len(bits)==3:
    d=bits[1]
elif len(bits)==2:
    d=bits[0]
else:
    d=parsed.netloc
full=os.path.join(d,h[1:])
try:
    os.makedirs(full)
except Exception as e:
    print >> sys.stderr, e
chunkedFetchUrl(url, local_filename=os.path.join(full, t))
