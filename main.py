#!/usr/bin/env python3

import sys
from wsgiref.simple_server import make_server


def get_ip(environ, start_response):
    resp_env = {}
    headers = [('Content-type', 'text/plain; charset=utf-8')]

    if environ['PATH_INFO'] != '/':
        status = '404 Not Found'
        start_response(status, headers)
        return ['ERROR 404'.encode('utf-8')]
    else:
        status = '200 OK'
        start_response(status, headers)
        if 'HTTP_X_FORWARDED_FOR' in environ:
            return [environ['HTTP_X_FORWARDED_FOR'].split(',')[0].encode('utf-8')]
        else:
            return [environ['REMOTE_ADDR'].encode('utf-8')]

if __name__ == '__main__':
    IP = "127.0.0.1"
    PORT = 5000
    if len(sys.argv) == 2:
        PORT = int(sys.argv[1])
    with make_server('', PORT, get_ip) as httpd:
        print(f'Serving HTTP on http://0.0.0.0:{PORT}')
        httpd.serve_forever()
