from tortoise import fields


class UUIDMixin:
    id = fields.UUIDField(pk=True)
