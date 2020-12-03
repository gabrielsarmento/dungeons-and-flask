from uuid import uuid4

from app.core.api import BaseHandler
from app.helpers.spells import serialize_spell_payload


class SpellHandler(BaseHandler):  # noqa
    def post(self):
        spell = serialize_spell_payload(self.request.body)
        spell['id'] = str(uuid4())

        self.set_status(201)
        self.write(spell)
