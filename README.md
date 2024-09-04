# CRUD API Development with Django and MongoDB

## Overview

This project is a technical assessment focused on developing a robust CRUD (Create, Read, Update, Delete) API for managing a collection of items stored in a MongoDB database using Django and Django REST Framework. The API includes comprehensive documentation, testing, and error handling. Additionally, advanced features such as filtering, searching, and pagination are implemented.

### Features

**CRUD Operations**: Create, Read, Update, and Delete items.
**MongoDB Integration**: Uses djongo to connect Django models to MongoDB.
**Advanced Features**: Filtering, searching, and pagination of items.
**Swagger Documentation**: Auto-generated API documentation available at /swagger/.
**Comprehensive Testing**: Unit tests for CRUD operations, pagination, filtering, and edge cases.
**Error Handling**: Meaningful error messages for invalid requests.

### Requirements

Django 4.x
Django REST Framework
Djongo
DRF-YASG (for Swagger documentation)
MongoDB

## Setup Instructions

1. ### Clone the Repository

   git clone [Put in the link to your repo]
   cd myapp

2. ### Create a Virtual Environment

   python -m venv venv
   source venv/bin/activate # **On Windows use** `venv\Scripts\activate`

3. ### Install Dependencies

   pip install -r requirements.txt

4. ### Configure MongoDB

   Create a .env file in the project root with the following content:
   MONGO_DB_NAME=your_mongo_db_name
   MONGO_DB_USER=your_mongo_db_user
   MONGO_DB_PASSWORD=your_mongo_db_password
   MONGO_DB_HOST=your_mongo_db_host
   MONGO_DB_PORT=your_mongo_db_port

5. ### Run Migrations

   python manage.py makemigrations
   python manage.py migrate

6. ### Run the Development Server

   cd myapp
   python manage.py runserver

7. ### Access the API

   The API can be accessed at http://localhost:8000/api/items/.

8. ### Swagger Documentation
   The Swagger UI can be accessed at http://localhost:8000/swagger/.

## API Endpoints

-**Create Item**: POST /api/items/ -**List Items**: GET /api/items/ -**Retrieve Item**: GET /api/items/{id}/ -**Update Item**: PUT /api/items/{id}/ -**Delete Item**: DELETE /api/items/{id}/ -**Swagger Documentation**: GET /swagger/

## Example Requests and Responses

### Create Item

#### Request:

POST /api/items/

{
"name": "Catherine Pugh",
"description": "Software Engineer"
"last_modified_by": null
}

#### Response:

{
"id": 1,
"name": "Catherine Pugh",
"description": "Software Engineer",
"created_at": "2024-09-03T13:51:31.830162Z",
"updated_at": "2024-09-03T13:51:31.830162Z",
"last_modified_by": null
}

### List Items

#### Request:

    GET /api/items/

#### Response:

[
{
"id": 1,
"name": "Catherine Pugh",
"description": "Software Engineer",
"created_at": "2024-09-03T13:51:31.830162Z",
"updated_at": "2024-09-03T13:51:31.830162Z",
"last_modified_by": null
}
]

## Testing

Unit tests are written using Django's test framework. To run the tests:
python manage.py test

### Tests cover:

- CRUD operations
- Pagination
- Filtering and searching
- Validation errors
