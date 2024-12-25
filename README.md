
# Flask API for Library Management System 

## Project Overview
This project is a simple **Library Management System** built with **Flask**, which allows users to perform CRUD operations (Create, Read, Update, Delete) on books and members. It includes JWT token-based authentication for secure access to the API, and it supports search functionality and pagination for books.

## Features
- **CRUD operations** for managing books and members.
- **Search functionality** for books by title or author.
- **Pagination** for book listings to improve performance.
- **Token-based authentication** using JWT.

---

## How to Run the Project

### 1. Clone the Repository
First, clone the repository to your local machine:

```bash
git clone https://github.com/ankitpareek054/library.git
cd library
```

### 2. Install Dependencies
The project uses Python and Flask, so you need to install the required dependencies. It is recommended to create a virtual environment to manage dependencies.

#### Install Python Dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

The `requirements.txt` file includes necessary libraries such as `Flask`, `Flask-SQLAlchemy`, and `PyJWT`.

### 3. Set Up the Database
Before running the project, you need to set up the database. You can initialize it by running the following command:

```bash
flask shell
>>> from models import db
>>> db.create_all()
>>> exit()
```

This will create the `library.db` file and the necessary tables in the database.

### 4. Running the Application
After setting up the database, you can run the Flask application:

```bash
python app.py
```

The server will start running at `http://127.0.0.1:5000`. You can now access the API and perform CRUD operations.

---

## Design Choices

1. **Flask Framework**: Flask is used for this project because it's lightweight and easy to set up, making it ideal for building small and medium-sized web applications. It also allows flexibility in adding features like JWT authentication and pagination.

2. **SQLAlchemy**: SQLAlchemy is used as the ORM (Object Relational Mapper) for interacting with the SQLite database. It provides an easy-to-use interface for querying and managing data.

3. **JWT Authentication**: JSON Web Tokens (JWT) are used for secure token-based authentication. The JWT is sent with each request to verify the user's identity. This ensures that only authenticated users can perform actions like adding, updating, or deleting books and members.

4. **SQLite Database**: SQLite is used for the database because it is simple to set up and suitable for smaller applications. It doesn't require a separate database server, making it easy to manage in a development environment.

5. **Search and Pagination**: The search functionality allows users to find books by title or author. Pagination is implemented to limit the number of books returned per request, improving performance when the number of books in the database grows.

6. **Flask Blueprint**: Although not explicitly used here, Flask's Blueprint feature could be used in future versions to organize the application into modular components, making it easier to scale and manage.

---

## Assumptions and Limitations

### Assumptions
1. **Token Generation**: The project assumes that users are generating their JWT tokens manually (outside the scope of this project). In real-world applications, you'd likely include a login API that generates tokens for authenticated users.

2. **Admin Role**: This project doesn't implement role-based access control (RBAC). All users have the same permissions, meaning they can access and modify data if they provide a valid JWT.

3. **Data Validation**: This project includes basic validation for required fields (e.g., title and author for books, name and email for members), but more robust validation can be added (e.g., validating email format).

4. **No Token Expiry**: The JWT used in this project does not expire. In a production system, you would want to implement token expiry and refresh tokens for security.

### Limitations
1. **No User Authentication**: The project doesn't implement user authentication, so it doesn't track who is logged in. The `token_required` decorator simply checks for the presence of a valid token but doesn’t associate it with a specific user or role.

2. **Basic Features**: The project does not include advanced features such as overdue book tracking, fines, or email notifications. It serves as a basic CRUD system for managing books and members.

3. **Scalability**: Since the project uses SQLite, it may not scale well with a large number of concurrent users or data. For larger-scale projects, consider using more robust databases like PostgreSQL or MySQL.

4. **No Frontend**: This project does not include a user interface (UI). It is an API-only application, so you need to interact with it via HTTP requests (e.g., using tools like Postman or Curl).

---

## API Endpoints

### Books
- **GET `/books`**: List all books (supports search by title/author and pagination).
- **POST `/books`**: Add a new book (requires a valid token).
- **GET `/books/<id>`**: Retrieve a specific book (requires a valid token).
- **PUT `/books/<id>`**: Update a specific book (requires a valid token).
- **DELETE `/books/<id>`**: Delete a specific book (requires a valid token).

### Members
- **GET `/members`**: List all members (requires a valid token).
- **POST `/members`**: Add a new member (requires a valid token).

---

## Troubleshooting

### Common Errors:
1. **Token is invalid!**: Ensure that you are sending a valid JWT token in the `x-access-token` header with each request.
2. **No module named 'jwt'**: If you see this error, ensure that you have installed the `PyJWT` library by running `pip install PyJWT`.

