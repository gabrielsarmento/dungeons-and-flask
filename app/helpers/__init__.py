from marshmallow import ValidationError, schema

from app.core.exception import PayloadValidationException


def serialize_payload(serializer: schema, payload: str) -> dict:
    try:
        dict_payload = serializer().loads(payload)
        return dict_payload
    except ValidationError as e:
        raise PayloadValidationException(metadata=e.messages)
