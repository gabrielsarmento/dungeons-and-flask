from tornado.web import RequestHandler

from app.core.database import get_db_session
from app.core.exception import BaseApiException


class BaseHandler(RequestHandler):  # noqa
    """
    Base handler gonna to be used instead of RequestHandler.
    """

    def write_error(self, status_code, **kwargs):
        error = kwargs.get('exc_info')[1]
        if isinstance(error, BaseApiException):
            self.set_status(error.status_code)
            self.write({
                'message': error.message,
                'metadata': error.metadata
            })
        # raise error

    def prepare(self):
        self.db = get_db_session()

    def on_finish(self) -> None:
        self.db.close()
