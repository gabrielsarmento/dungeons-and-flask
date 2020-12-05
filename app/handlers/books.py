from http import HTTPStatus
from uuid import uuid4

from app.core.api import BaseHandler
from app.handlers.serializers import BookSchema
from app.helpers import serialize_payload
from models.models import BookModel


class BookHandler(BaseHandler):  # noqa
    def post(self):
        book = serialize_payload(BookSchema, self.request.body)
        book['id'] = str(uuid4())

        book_db = BookModel(**book)
        self.db.add(book_db)
        self.db.commit()

        self.db.close()

        self.set_status(HTTPStatus.CREATED)
        self.write(book)
