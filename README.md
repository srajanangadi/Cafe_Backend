☕ Cafe Backend API
-----------------------------------------------------------
A RESTful backend API for a Cafe/Store management system built using Flask, MySQL, and JWT Authentication.
This project provides endpoints to manage users and items, with secure authentication and modular architecture.

🚀 Features
---------------------
🔐 JWT Authentication
- User login and protected endpoints
- Token revocation using blocklist
👤 User Management
- User registration
- Login system
- Secure authentication using JWT
📦 Item Management
- Create items
- Retrieve items
- Update item details
- Delete items
🧩 Modular Project Structure
- Separate resources, schemas, and database logic
- Easy to maintain and extend
📄 API Documentation
- Built using Flask-Smorest with OpenAPI support

🛠️ Tech Stack
--------------------------
Backend Framework: Flask
Database: MySQL
ORM / DB Connector: mysql-connector-python
Authentication: Flask-JWT-Extended
API Documentation: Flask-Smorest + Marshmallow
Environment Management: python-dotenv

Cafe Backend/
│
├── app.py                # Main application entry point
├── blocklist.py          # JWT token blocklist
├── schemas.py            # Marshmallow schemas
├── requirements.txt      # Project dependencies
│
├── db/
│   ├── items_db.py       # Item database operations
│   └── users_db.py       # User database operations
│
└── resources/
    ├── items.py          # Item API routes
    └── users.py          # User API routes

🔑 Authentication Flow
---------------------------
Register a user
Login to receive a JWT token
Use the token to access protected endpoints
Logout will revoke the token using blocklist

🔒 Security
---------------------------
JWT based authentication
Token revocation with blocklist
Input validation using Marshmallow schemas

📦 Dependencies
-----------------------------
Main libraries used:

Flask
Flask-JWT-Extended
Flask-Smorest
Marshmallow
SQLAlchemy
mysql-connector-python
See requirements.txt for full list.

📈 Future Improvements
------------------------------
Add order management
Add role-based access (admin/staff)
Add product categories
Dockerize the application
Deploy using cloud services

👨‍💻 Author
Srajankumar Angadi
Developed as a backend REST API project using Flask and MySQL.
