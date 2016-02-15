#!/usr/bin/env python

from wsgiref.simple_server import make_server


def get_ip(environ, start_response):
    response_headers = [('Content-type', 'text/plain')]

    if environ['PATH_INFO'] != '/':
        status = '404 Not Found'
        start_response(status, response_headers)
        return ['ERROR 404']
    else:
        status = '200 OK'
        start_response(status, response_headers)
        if 'HTTP_X_FORWARDED_FOR' in environ:
            return [environ['HTTP_X_FORWARDED_FOR'].split(',')[0]]
        else:
            return [environ['REMOTE_ADDR']]


if __name__ == '__main__':
    httpd = make_server('', 5000, get_ip)
    print 'Serving HTTP on port 5000...'
    httpd.serve_forever()
