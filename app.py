# -*-coding: utf-8 -*-

# WSGI web server gateway interface

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    print environ['PATH_INFO']
    return '<h1>Hello %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')

