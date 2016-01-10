#!/usr/bin/env python

from wsgiref.simple_server import make_server


def get_ip(environ, start_response):
  status = '200 OK'
  response_headers = [('Content-type', 'text/plain')]
  start_response(status, response_headers)
  if 'HTTP_X_FORWARDED_FOR' in environ:
    return [environ['HTTP_X_FORWARDED_FOR'].split(',')[0]]
  else:
    return [environ['REMOTE_ADDR']]


if __name__ == '__main__':
  httpd = make_server('', 8000, get_ip)
  print 'Serving HTTP on port 8000...'
  httpd.serve_forever()
