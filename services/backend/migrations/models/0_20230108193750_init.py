from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "legalstatus" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "name" VARCHAR(20) NOT NULL UNIQUE
);
COMMENT ON COLUMN "legalstatus"."name" IS 'Nom';
CREATE TABLE IF NOT EXISTS "user" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "identifier" SMALLINT NOT NULL UNIQUE,
    "operation" VARCHAR(100),
    "first_name" VARCHAR(100),
    "last_name" VARCHAR(100),
    "street_number" VARCHAR(10),
    "street_name" VARCHAR(100),
    "postal_code" INT NOT NULL,
    "city" VARCHAR(100) NOT NULL,
    "last_updated_on" DATE,
    "membership_year" SMALLINT NOT NULL,
    "password" VARCHAR(128) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "modified_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "legal_status_id" UUID NOT NULL REFERENCES "legalstatus" ("id") ON DELETE CASCADE
);
COMMENT ON COLUMN "user"."identifier" IS 'Identifiant';
COMMENT ON COLUMN "user"."operation" IS 'Exploitation';
COMMENT ON COLUMN "user"."first_name" IS 'Prénom';
COMMENT ON COLUMN "user"."last_name" IS 'Nom';
COMMENT ON COLUMN "user"."street_number" IS 'Numéro de rue';
COMMENT ON COLUMN "user"."street_name" IS 'Rue';
COMMENT ON COLUMN "user"."postal_code" IS 'Code postal';
COMMENT ON COLUMN "user"."city" IS 'Ville';
COMMENT ON COLUMN "user"."last_updated_on" IS 'Date de dernière mise à jour';
COMMENT ON COLUMN "user"."membership_year" IS 'Année d''adhésion';
COMMENT ON COLUMN "user"."password" IS 'Mot de passe';
COMMENT ON COLUMN "user"."created_at" IS 'Date de création';
COMMENT ON COLUMN "user"."modified_at" IS 'Date de mise à jour';
COMMENT ON COLUMN "user"."legal_status_id" IS 'Statut juridique';
CREATE TABLE IF NOT EXISTS "email" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "value" VARCHAR(10) NOT NULL UNIQUE,
    "name" VARCHAR(20) NOT NULL,
    "user_id" UUID NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
COMMENT ON COLUMN "email"."value" IS 'Valeur';
COMMENT ON COLUMN "email"."name" IS 'Nom';
COMMENT ON COLUMN "email"."user_id" IS 'Utilisateur';
CREATE TABLE IF NOT EXISTS "phone" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "value" VARCHAR(10) NOT NULL UNIQUE,
    "name" VARCHAR(20) NOT NULL,
    "user_id" UUID NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
COMMENT ON COLUMN "phone"."value" IS 'Valeur';
COMMENT ON COLUMN "phone"."name" IS 'Nom';
COMMENT ON COLUMN "phone"."user_id" IS 'Utilisateur';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
