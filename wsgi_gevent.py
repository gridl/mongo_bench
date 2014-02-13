#!/usr/bin/env python
from gevent import monkey
monkey.patch_all()

from gevent.wsgi import WSGIServer
from pymongo import MongoClient


db = MongoClient(use_greenlets=True)['documents']


def application(environ, start_response):
    data = str(db.items.find_one({})['data'])

    start_response(
        '200 OK',
        [
            ('Content-Type', 'text/plain'),
            ('Content-Length', str(len(data)))
        ]
    )

    yield data


if __name__ == '__main__':
    WSGIServer(
        ('127.0.0.1', 7777),
        application
    ).serve_forever()
