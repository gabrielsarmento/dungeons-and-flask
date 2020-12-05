from marshmallow import Schema, fields


class BookSchema(Schema):
    name = fields.String(required=True)


class SpellSchema(Schema):
    name = fields.String(required=True)
    level = fields.Integer(required=True)
    description = fields.String(required=True)
    casting_time = fields.String(required=True)
    components = fields.String(required=True)
    duration = fields.String(required=True)
    range = fields.String(required=True)
    is_ritual = fields.Boolean(default=False)
    book_id = fields.String(required=True)
    school_id = fields.String(required=True)


class SchoolSchema(Schema):
    name = fields.String(required=True)
    book_id = fields.String(required=True)
