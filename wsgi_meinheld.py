#!/usr/bin/env python
from meinheld import server
from pymongo import MongoClient


db = MongoClient()['documents']


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
    server.listen(('127.0.0.1', 7777))
    server.run(application)
