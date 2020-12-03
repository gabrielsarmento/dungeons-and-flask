from marshmallow import ValidationError

from app.exceptions.spells import SpellPayloadValidationException
from app.handlers.serializers import SpellSchema


def serialize_spell_payload(spell_json: str) -> dict:
    try:
        spell = SpellSchema().loads(spell_json)
        return spell
    except ValidationError as e:
        raise SpellPayloadValidationException(metadata=e.messages)
