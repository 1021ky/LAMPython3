#!/usr/bin/env python
#
# Ansible managed file, do not edit directly
#

from sqlalchemy import create_engine
import json

class UserDAO(object):
    def __init__(self):
        self._engine=create_engine('mysql://developer:developer@192.168.20.11:3306/SampleDB')

    def getUser(self):
        result = self._engine.execute('SELECT * FROM User')
        return [r for r in result]

def application(environ, start_response):
    status = '200 OK'

    dao = UserDAO()
    users = dao.getUser()
    body={'users':[]}
    for user in users:
        id, username, email = user
        d = {
                'id': str(id),
                'username': username,
                'email': email
            }
        body['users'].append(d)
    content = json.dumps(body).encode('utf-8')
    response_headers = [('Content-type', 'application/json'),
                        ('Content-Length', str(len(content)))]
    start_response(status, response_headers)
    return [content]