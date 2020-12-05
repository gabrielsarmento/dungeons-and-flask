from http import HTTPStatus
from uuid import uuid4

from app.core.api import BaseHandler
from app.handlers.serializers import SpellSchema
from app.helpers import serialize_payload
from app.helpers.books import get_book_or_404
from app.helpers.schools import get_school_or_404
from models.models import SpellModel


class SpellHandler(BaseHandler):  # noqa
    def post(self):
        spell = serialize_payload(SpellSchema, self.request.body)
        get_book_or_404(self.db, spell['book_id'])
        get_school_or_404(self.db, spell['school_id'])
        spell['id'] = str(uuid4())

        spell_db = SpellModel(**spell)

        self.db.add(spell_db)
        self.db.commit()

        self.set_status(HTTPStatus.CREATED)
        self.write(spell)
