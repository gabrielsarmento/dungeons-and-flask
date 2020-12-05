from http import HTTPStatus
from uuid import uuid4

from app.core.api import BaseHandler
from app.handlers.serializers import SchoolSchema
from app.helpers import serialize_payload
from app.helpers.books import get_book_or_404
from models.models import SchoolModel


class SchoolHandler(BaseHandler):  # noqa
    def post(self):
        school = serialize_payload(SchoolSchema, self.request.body)
        school['id'] = str(uuid4())

        get_book_or_404(self.db, school['book_id'])

        school_db = SchoolModel(**school)

        self.db.add(school_db)
        self.db.commit()

        self.set_status(HTTPStatus.CREATED)
        self.write(school)
