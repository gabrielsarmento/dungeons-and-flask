from app.core.exception import BaseApiException


class SpellPayloadValidationException(BaseApiException):
    message = 'Spell payload validation error.'
    status_code = 400
