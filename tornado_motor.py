#!/usr/bin/env python
import tornado.web
import tornado.ioloop
import motor


class IndexRequestHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.settings['db']

    @tornado.web.asynchronous
    def get(self):
        self.db.items.find_one(
            {},
            callback=self._on_find_one
        )

    def _on_find_one(self, result, error):
        self.write(result['data'])
        self.finish()


if __name__ == '__main__':
    db = motor.MotorClient().open_sync()['documents']

    application = tornado.web.Application(
        [
            (r'/', IndexRequestHandler)
        ],
        db=db
    )

    application.listen(7777)

    tornado.ioloop.IOLoop.instance().start()
