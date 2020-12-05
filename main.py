from tornado.ioloop import IOLoop
from tornado.web import Application

from app.handlers.books import BookHandler
from app.handlers.schools import SchoolHandler
from app.handlers.spells import SpellHandler

urls = [
    (r'/books', BookHandler),
    (r'/spells', SpellHandler),
    (r'/schools', SchoolHandler)
]


def create_app() -> Application:
    api = Application(
        handlers=urls,
        debug=True
    )
    return api


if __name__ == '__main__':
    app = create_app()
    app.listen(8888)
    IOLoop.current().start()
