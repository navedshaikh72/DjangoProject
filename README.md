## Django Login System 

A comprehensive Django web application that implements a complete user authentication and management system with CRUD operations. This project demonstrates best practices in Django development including models, views, templates, URL routing, and database operations.

## Features

User Authentication

User signup with email validation
Secure login functionality
Success messages and redirects


User Management (CRUD)

Create new user accounts
Read/Retrieve all users
Retrieve single user by email
Update user details (email and password)
Delete user accounts


Admin Panel

Django admin interface for user management
Superuser account management
Direct database access


Professional UI

Clean HTML templates
Form validation
Error handling and display
User-friendly interface


Technologies Used

Backend: Django 4.2.29
Database: SQLite3
Language: Python 3.9
Frontend: HTML5, CSS3
Testing: Postman
Version Control: Git & GitHub


Project Structure
Login_System/
├── Login_System/                 # Project configuration
│   ├── settings.py              # Django settings
│   ├── urls.py                  # Main URL configuration
│   ├── wsgi.py                  # WSGI configuration
│   └── asgi.py
│
├── Loginify/                     # Django application
│   ├── models.py                # UserDetails model
│   ├── views.py                 # All view functions
│   ├── urls.py                  # App URL patterns
│   ├── admin.py                 # Admin configuration
│   ├── apps.py
│   ├── migrations/              # Database migrations
│   │   └── 0001_initial.py
│   └── templates/Loginify/      # HTML templates
│       ├── signup.html
│       ├── login.html
│       ├── success.html
│       ├── all_users.html
│       ├── user_detail.html
│       └── update_user.html
│
├── db.sqlite3                    # SQLite database
├── manage.py                     # Django management script
└── DjangoAssignment/             # Virtual environment

Installation & Setup 
Prerequisites

Python 3.8 or higher
pip (Python package manager)
Git

Step 1: Clone Repository
bashgit clone https://github.com/YOUR_USERNAME/DjangoProject.git
cd Login_System
Step 2: Create Virtual Environment
Windows:
bashpython -m venv DjangoAssignment
DjangoAssignment\Scripts\activate
Mac/Linux:
bashpython -m venv DjangoAssignment
source DjangoAssignment/bin/activate
Step 3: Install Dependencies
bashpip install django
Step 4: Apply Migrations
bashpython manage.py migrate
Step 5: Create Superuser (Optional)
bashpython manage.py createsuperuser
Follow the prompts to create admin credentials.
Step 6: Run Server
bashpython manage.py runserver
Server starts at: http://127.0.0.1:8000/

##Usage
Accessing the Application
Home Page:
http://127.0.0.1:8000/
Displays: "Hello, world!"
Signup Page:
http://127.0.0.1:8000/app/signup/
Create a new account with username, email, and password.
Login Page:
http://127.0.0.1:8000/app/login/
Login with registered email and password.
Admin Panel:
http://127.0.0.1:8000/admin/
Manage users through Django admin interface.

##API Endpoints 

1. Get All Users
GET http://127.0.0.1:8000/app/all-users/
Returns: Table with all registered users
2. Get Single User by Email
GET http://127.0.0.1:8000/app/user/<email>/
Example:
GET http://127.0.0.1:8000/app/user/john@example.com/
Returns: User details (username, email)
3. Update User Details
POST http://127.0.0.1:8000/app/update/<username>/
Example:
POST http://127.0.0.1:8000/app/update/john/
Body (form-data):
email: newemail@example.com
password: newpassword123
Returns: Success message
4. Delete User
GET http://127.0.0.1:8000/app/delete/<email>/
Example:
GET http://127.0.0.1:8000/app/delete/john@example.com/
Returns: "User deleted successfully"

Database Model
UserDetails Model
pythonclass UserDetails(models.Model):
    username = CharField(max_length=50, primary_key=True)
    email = EmailField(unique=True)
    password = CharField(max_length=12, blank=True)
Fields:

username (String, Primary Key): Unique username
email (Email, Unique): User's email address
password (String): User's password


Testing with Postman
Prerequisites

Download Postman from: https://www.postman.com/downloads/

Test Cases
Test 1: GET All Users

Method: GET
URL: http://127.0.0.1:8000/app/all-users/
Expected Status: 200 OK
Response: HTML table with users

Test 2: GET Single User

Method: GET
URL: http://127.0.0.1:8000/app/user/test@example.com/
Expected Status: 200 OK
Response: User details page

Test 3: UPDATE User

Method: POST
URL: http://127.0.0.1:8000/app/update/testuser/
Body (form-data):

  email: newemail@example.com
  password: newpass123

Expected Status: 200 OK
Response: Success page

Test 4: DELETE User

Method: GET
URL: http://127.0.0.1:8000/app/delete/newemail@example.com/
Expected Status: 200 OK
Response: "User deleted successfully"


Key Features Explained 🎯
Signup Functionality

Validates unique username and email
Creates new user record in database
Redirects to login page after successful signup
Error handling for duplicate emails

Login Functionality

Validates email and password combination
Displays success message on correct credentials
Shows error message on invalid login
Secure password comparison

User Management

View all registered users
Search user by email
Update user information dynamically
Delete users with confirmation

Admin Interface

Manage users directly through Django admin
View user data in organized tables
Add, edit, delete users easily
Superuser access control


Common Issues & Solutions 🔧
Issue: Database Error
Solution:
bashpython manage.py migrate
Issue: Template Not Found
Solution: Ensure Loginify/templates/Loginify/ folder exists with all HTML files.
Issue: Port Already in Use
Solution:
bashpython manage.py runserver 8001
Then access: http://127.0.0.1:8001/
Issue: CSRF Token Error
Solution: CSRF is disabled for testing. Re-enable in production by uncommenting CSRF middleware in settings.py.

Future Enhancements 🚀

Implement password hashing (bcrypt)
Add email verification
Implement JWT authentication
Add user profile pictures
Implement session management
Add API using Django REST Framework
Implement role-based access control
Add unit tests
Deploy to production server


Security Notes ⚠️
Current Configuration (Development Only):

CSRF middleware is disabled for testing
Passwords are stored in plain text
Debug mode is enabled

For Production:

Enable CSRF protection
Use password hashing (Django's make_password)
Set DEBUG = False
Use environment variables for sensitive data
Implement HTTPS
Use secure cookies


Contributing 🤝

Fork the repository
Create a feature branch: git checkout -b feature/your-feature
Commit changes: git commit -m 'Add your feature'
Push to branch: git push origin feature/your-feature
Submit a pull request


Author ✍️
Name: Naved Asif Shaikh
Email: navedasifshaikh@example.com
GitHub: @navedshaikh72

License 📜
This project is open source and available under the MIT License.

Acknowledgments 🙏

Django Documentation: https://docs.djangoproject.com/
Consultadd Training Team
Django Community


Version History
v1.0.0 (March 12, 2026)

Initial release
Complete CRUD operations
User authentication system
Admin panel integration
Postman testing support