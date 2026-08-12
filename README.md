# Python Movies API

## Overview

Python Movies API is a Django REST framework application for managing movie data, genre categories, actor information, and user reviews. The project uses JWT token authentication to secure API endpoints and enforces model-level permissions for all operations.

## Architecture

The project is organized as a Django project named `app` with five main applications:

- `authentication` for token-based authentication endpoints
- `genres` for genre management
- `actors` for actor records
- `movies` for movie records and statistics
- `reviews` for movie reviews

Each application follows the standard Django REST framework structure with models, serializers, views, and URL routing. The root URL configuration in `app/urls.py` exposes a versioned API prefix at `/api/v1/`.

### Core design principles

- Django REST framework generic views are used for CRUD operations
- JSON Web Tokens are used for stateless authentication
- A custom permission class maps HTTP methods to Django model permissions
- Serialized model data is validated before saving
- Movie statistics are provided through a dedicated endpoint

## Data Model Summary

### Genre

- `name`: string

### Actor

- `name`: string
- `birthday`: date
- `nationality`: choice field with predefined country codes

### Movie

- `title`: string
- `genre`: foreign key to `Genre`
- `release_date`: date
- `actors`: many-to-many relationship to `Actor`
- `resume`: text
- `rate`: computed average review score exposed by the serializer

### Review

- `movie`: foreign key to `Movie`
- `stars`: integer validated between 0 and 5
- `comment`: text

## Authentication

Authentication is implemented using `djangorestframework-simplejwt`. All API views require an authenticated user and evaluate model permissions through the custom permission class defined in `app/permissions.py`.

The authentication endpoints are exposed at:

- `POST /api/v1/authentication/token/` to obtain an access token and a refresh token
- `POST /api/v1/authentication/token/refresh/` to refresh an expired access token
- `POST /api/v1/authentication/token/verify/` to verify a token

Access to all other API endpoints requires the `Authorization` header with a bearer token:

```
Authorization: Bearer <access_token>
```

## API Endpoints

### Genres

- `GET /api/v1/genres/` list genres
- `POST /api/v1/genres/` create a genre
- `GET /api/v1/genres/<id>/` retrieve a genre
- `PUT /api/v1/genres/<id>/` update a genre
- `PATCH /api/v1/genres/<id>/` partially update a genre
- `DELETE /api/v1/genres/<id>/` delete a genre

### Actors

- `GET /api/v1/actors/` list actors
- `POST /api/v1/actors/` create an actor
- `GET /api/v1/actors/<id>/` retrieve an actor
- `PUT /api/v1/actors/<id>/` update an actor
- `PATCH /api/v1/actors/<id>/` partially update an actor
- `DELETE /api/v1/actors/<id>/` delete an actor

### Movies

- `GET /api/v1/movies/` list movies
- `POST /api/v1/movies/` create a movie
- `GET /api/v1/movies/<id>/` retrieve a movie
- `PUT /api/v1/movies/<id>/` update a movie
- `PATCH /api/v1/movies/<id>/` partially update a movie
- `DELETE /api/v1/movies/<id>/` delete a movie
- `GET /api/v1/movies/stats/` retrieve aggregate movie statistics

The movie serializer also exposes a `rate` field that returns the average review score for each movie.

### Reviews

- `GET /api/v1/reviews/` list reviews
- `POST /api/v1/reviews/` create a review
- `GET /api/v1/reviews/<id>/` retrieve a review
- `PUT /api/v1/reviews/<id>/` update a review
- `PATCH /api/v1/reviews/<id>/` partially update a review
- `DELETE /api/v1/reviews/<id>/` delete a review

## Permissions

The custom permission class in `app/permissions.py` determines permission codes from the resource model and HTTP method. It checks the authenticated user against Django permissions such as:

- `add_<model>` for POST requests
- `change_<model>` for PUT and PATCH requests
- `delete_<model>` for DELETE requests
- `view_<model>` for GET requests

This enforces a model-level access policy for every endpoint.

## Settings and environment

The project loads environment variables from a `.env` file via `python-dotenv` in `app/settings.py`. The following variables are used:

- `SECRET_KEY`
- `DEBUG`

Database configuration uses SQLite and stores the local database file at `db.sqlite3`.

Static files are configured with `STATIC_URL = 'static/'` and `STATIC_ROOT = <base>/staticfiles`.

## Installation

1. Create and activate a Python virtual environment.
2. Install dependencies from `requirements.txt`.
3. Copy `.env.example` to `.env` and provide a secret key.
4. Run database migrations:

```bash
python manage.py migrate
```

5. Create a superuser or regular user to authenticate:

```bash
python manage.py createsuperuser
```

6. Start the development server:

```bash
python manage.py runserver
```

## Notes

- This project uses Django 6 and Django REST framework.
- Authentication is handled through JWT tokens, not session cookies.
- There is no dedicated user registration API in the current implementation. Users must be created via the Django admin or management commands.
- The `movies` API includes a dedicated statistics endpoint and review aggregation.
