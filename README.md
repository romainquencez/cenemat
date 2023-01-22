# Projet pour le CENEMAT

## Installation

Copier et compléter le fichier des variables d'environnement :

```shell
cp .env.example .env
```

Le compléter avec ces valeurs pour du développement local :

Clé | Valeur
---|---
POSTGRES_USER | cenemat
POSTGRES_PASSWORD | cenemat
POSTGRES_DB | cenemat
POSTGRES_PORT | 5432
FLYWAY_CLEAN_DISABLED | false
FASTAPI_ALLOW_ORIGIN | http://localhost:44325
JWT_SECRET_KEY | Générer une clé secrète

Récupérer les images Docker :

```shell
docker compose pull
```

Construire et lancer les conteneurs :

```shell
docker compose up -d --build
```

## Backend

### Installation

Les adresses suivantes sont accessibles :

* [Serveur web](http://localhost:8000) : `http://localhost:8000`
* [Swagger](http://localhost:8000/docs) : `http://localhost:8000/docs`

Suvi des logs :

```shell
docker compose logs -ft backend
```

### Vérifier les mise à jour

```shell
docker compose exec backend pip list --outdated
```

### Exécuter les tests

```shell
docker compose exec backend pytest .
```

## Frontend

Suvi des logs :

```shell
docker compose logs -ft frontend
```

L'application est disponible sur `http://localhost:9000`.

### Linter

Le linter peut être exécutée pour s'assurer que le code est conforme :

```shell
docker compose exec frontend npm run lint
```

### Formatter

```shell
docker compose exec frontend npm run format
```

### Construire la version de production

```shell
docker compose exec frontend quasar build
```

### Liens utiles

* [Configuring quasar.config.js](https://v2.quasar.dev/quasar-cli-vite/quasar-config-js)

## Migrations

Les migrations sont gérées par [Flyway](https://flywaydb.org). Elles sont validées et jouées à chaque lancement des containers avec `docker compose up -d`.

Les nouvelles migrations sont à ajouter dans le répertoire `services/sql` et doivent être nommées selon [les règles de Flyway](https://flywaydb.org/documentation/concepts/migrations.html#sql-based-migrations).

Une fois le fichier `.sql` créé, la migration peut être jouée à l'aide la commande `migrate`.

### Commandes

### Migrate

Jouer les migrations :

```shell
docker compose run migrations migrate
```

[Documentation de la commande migrate](https://flywaydb.org/documentation/command/migrate)

### Clean

Ré-initialiser la base de données :

```shell
docker compose run migrations clean
```

[Documentation de la commande clean](https://flywaydb.org/documentation/command/clean)

### Info

Afficher des informations concernant l'état des migrations :

```shell
docker compose run migrations info
```

Exemple de rendu :

```shell
Flyway is up to date
Flyway Community Edition 9.11.0 by Redgate
See what's new here: https://flywaydb.org/documentation/learnmore/releaseNotes#9.11.0

Database: jdbc:postgresql://db:5432/cenemat (PostgreSQL 15.1)
Schema version: 3

+-----------+---------+---------------------------+------+---------------------+---------+----------+
| Category  | Version | Description               | Type | Installed On        | State   | Undoable |
+-----------+---------+---------------------------+------+---------------------+---------+----------+
| Versioned | 1       | create legal status table | SQL  | 2023-01-17 21:19:08 | Success | No       |
| Versioned | 2       | create users table        | SQL  | 2023-01-17 21:19:08 | Success | No       |
| Versioned | 3       | create phones table       | SQL  | 2023-01-17 21:19:08 | Success | No       |
+-----------+---------+---------------------------+------+---------------------+---------+----------+
```

[Documentation de la commande info](https://flywaydb.org/documentation/command/info)

### Validate

Valider la cohérence des migrations vis-à-vis de la base de données :

```shell
docker compose run migrations validate
```

Note : la commande `migrate` effectue déjà une validation avant d'exécuter les migrations.

[Documentation de la commande validate](https://flywaydb.org/documentation/command/validate)

## Pre-commit

### Installation

```shell
pre-commit install
```

### Nettoyage du cache

```shell
pre-commit cache
```

### Mise à jour des hooks

```shell
pre-commit autoupdate
```

### Exécution sur tout le projet

```shell
pre-commit run --all-files
```

### Liens utiles

* [Documentation](https://pre-commit.com)

# Références

* [Developing a Single Page App with FastAPI and Vue.js](https://testdriven.io/blog/developing-a-single-page-app-with-fastapi-and-vuejs/#vue-setup)
* [Developing and Testing an Asynchronous API with FastAPI and Pytest](https://testdriven.io/blog/fastapi-crud/)
* [Implementing Flyway with Docker](https://heavylion.medium.com/implementing-flyway-with-docker-8ae256ce634f)
*
