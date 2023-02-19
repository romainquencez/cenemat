CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS "legal_status" (
  "id" UUID NOT NULL PRIMARY KEY DEFAULT uuid_generate_v4(),
  "name" VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS "user" (
  "id" UUID NOT NULL PRIMARY KEY DEFAULT uuid_generate_v4(),
  "identifier" SMALLINT NOT NULL UNIQUE,
  "email" VARCHAR(100) NOT NULL UNIQUE,
  "farm" VARCHAR(100),
  "first_name" VARCHAR(100),
  "last_name" VARCHAR(100),
  "last_updated_on" DATE,
  "membership_year" SMALLINT NOT NULL,
  "password" VARCHAR(128) NOT NULL,
  "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "modified_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "legal_status_id" UUID NOT NULL REFERENCES "legal_status" ("id") ON DELETE CASCADE,
  "is_admin" BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS "phone" (
   "id" UUID NOT NULL  PRIMARY KEY DEFAULT uuid_generate_v4(),
   "value" VARCHAR(10) NOT NULL UNIQUE,
   "name" VARCHAR(20) NOT NULL,
   "user_id" UUID NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "address" (
    "id"            UUID         NOT NULL PRIMARY KEY DEFAULT uuid_generate_v4(),
    "street_number" VARCHAR(10),
    "street_name"   VARCHAR(100),
    "postal_code"   INT          NOT NULL,
    "city"          VARCHAR(100) NOT NULL,
    "user_id" UUID NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
