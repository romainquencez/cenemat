# Projet pour le CENEMAT

## Installation

Copier et compléter le fichier des variables d'environnement :

```shell
cp .env.example .env
```

Le compléter avec ces valeurs pour du développement local :

Clé | Valeur
---|---
DATABASE_URL | postgres://cenemat:cenemat@db:5432/cenemat
FASTAPI_ALLOW_ORIGIN | http://localhost:8080
JWT_SECRET_KEY | Générer une clé secrète

Récupérer les images Docker :

```shell
docker-compose pull
```

Construire et lancer les conteneurs :

```shell
docker-compose up -d --build
```

## Backend

### Installation

Copier le fichier des variables d'environnement `env.example` et le compléter selon les besoins.

L'application est disponible sur `localhost:8000`.

Les adresses suivantes sont accessibles :

* [Serveur web](http://localhost:5000) : `http://localhost:5000`
* [Swagger](http://localhost:5000/docs) : `http://localhost:5000/docs`

Suvi des logs :

```shell
docker-compose logs -ft backend
```

### Vérifier les mise à jour

```shell
docker-compose exec backend pip list --outdated
```

### Initialiser la configuration Aerich

```shell
docker-compose exec backend aerich init -t src.database.config.TORTOISE_ORM
```

### Générer les migrations

```shell
docker-compose exec backend aerich init-db
```

### Exécuter les migrations

```shell
docker-compose exec backend aerich migrate
docker-compose exec backend aerich upgrade
```

### Exécuter les tests

```shell
docker-compose exec backend pytest .
```

## Frontend

Suvi des logs :

```shell
docker-compose logs -ft frontend
```

L'application est disponible sur `localhost:9000`.

### Linter

Le linter peut être exécutée pour s'assurer que le code est conforme :

```shell
docker-compose exec frontend npm run lint
```

### Formatter

```shell
docker-compose exec frontend npm run format
```

### Construire la version de production

```shell
docker-compose exec frontend quasar build
```

### Liens utiles

* [Configuring quasar.config.js](https://v2.quasar.dev/quasar-cli-vite/quasar-config-js)

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
