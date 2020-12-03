from marshmallow import Schema, fields


class SpellSchema(Schema):
    name = fields.String(required=True)
    level = fields.Integer(required=True)
    description = fields.String(required=True)
    casting_time = fields.String(required=True)
    components = fields.String(required=True)
    duration = fields.String(required=True)
    school = fields.String(required=True)
    range = fields.String(required=True)
    is_ritual = fields.Boolean(default=False)
