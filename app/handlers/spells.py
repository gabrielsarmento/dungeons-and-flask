from uuid import uuid4

from app.core.api import BaseHandler
from app.handlers.serializers import SpellSchema
from app.helpers import serialize_payload


class SpellHandler(BaseHandler):  # noqa
    def post(self):
        spell = serialize_payload(SpellSchema, self.request.body)
        spell['id'] = str(uuid4())

        self.set_status(201)
        self.write(spell)
