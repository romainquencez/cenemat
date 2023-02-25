ALTER TABLE public.user
DROP COLUMN farm,
DROP COLUMN legal_status_id;

CREATE TABLE IF NOT EXISTS "farm" (
   "id" UUID NOT NULL PRIMARY KEY DEFAULT uuid_generate_v4(),
   "legal_status_id" UUID NOT NULL REFERENCES "legal_status" ("id") ON DELETE CASCADE,
   "name" VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS "user_farm" (
    "farm_id" UUID NOT NULL REFERENCES "farm" ("id") ON DELETE CASCADE,
    "user_id" UUID NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
