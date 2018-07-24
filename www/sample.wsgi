#!/usr/bin/env python
#
# Ansible managed file, do not edit directly
#

def application(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/plain')])
    return [b'Hello, world']