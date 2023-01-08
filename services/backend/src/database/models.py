from src.database.mixins import UUIDMixin
from tortoise import fields, models


class LegalStatus(models.Model, UUIDMixin):
    name = fields.CharField(description="Nom", max_length=20, unique=True)


class BaseContact(models.Model, UUIDMixin):
    value = fields.CharField(description="Valeur", max_length=10, unique=True)
    name = fields.CharField(description="Nom", max_length=20)

    class Meta:
        abstract = True


class Phone(BaseContact):
    user = fields.ForeignKeyField(
        "models.User", description="Utilisateur", related_name="phones"
    )


class Email(BaseContact):
    user = fields.ForeignKeyField(
        "models.User", description="Utilisateur", related_name="emails"
    )


class User(models.Model, UUIDMixin):
    identifier = fields.SmallIntField(description="Identifiant", unique=True)
    legal_status = fields.ForeignKeyField(
        "models.LegalStatus", description="Statut juridique", related_name="users"
    )
    operation = fields.CharField(description="Exploitation", max_length=100, null=True)
    first_name = fields.CharField(description="Prénom", max_length=100, null=True)
    last_name = fields.CharField(description="Nom", max_length=100, null=True)
    street_number = fields.CharField(
        description="Numéro de rue", max_length=10, null=True
    )
    street_name = fields.CharField(description="Rue", max_length=100, null=True)
    postal_code = fields.IntField(description="Code postal")
    city = fields.CharField(description="Ville", max_length=100)
    last_updated_on = fields.DateField(
        description="Date de dernière mise à jour", null=True
    )
    membership_year = fields.SmallIntField(description="Année d'adhésion")
    password = fields.CharField(description="Mot de passe", max_length=128)
    created_at = fields.DatetimeField(auto_now_add=True, description="Date de création")
    modified_at = fields.DatetimeField(auto_now=True, description="Date de mise à jour")
