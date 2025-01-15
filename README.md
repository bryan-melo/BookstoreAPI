# BookstoreAPI

## Objective:
Create a RESTful API for managing a bookstore. Aiming to practicing backend fundamentals such as HTTP requests, database interaction, and backend features such as authentication and validation

## Features:
1. Book Management:
* Add, update, delete, and list books.
* Each book will have attributes such as title, author, ISBN, and stock.

2. User Management:
* User registration and login with password hashing.
* Role-based access control (e.g, Admin and Customer),

3. Search and Filters:
* Search books by title or author.
* Filter books by genre or availability.

4. Order Management:
* Customers can place orders for books.
* Admins can view all orders.

## Technologies and Tools:
* Framework: FastAPI.
* Database: PostgreSQL with SQLAlchemy for ORM.
* Authentication: JWT (JSON Web Tokens).
* Environment Management: Docker
* Documentation: Swagger UI (built-in with Fast API).
* Testing: pytest.