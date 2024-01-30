
# Flask User Authentication App

This is a simple Flask web application for user authentication, utilizing Flask-SQLAlchemy for database management, Flask-Login for user sessions, Flask-WTF for form handling, and Flask-Bcrypt for password hashing.

## Getting Started

### Prerequisites

Make sure you have Python installed on your machine. You can install the required dependencies using the following command:


Open your web browser and go to https://signup-page-j6hd.onrender.com/ to access the application.

Features
User registration with form validation.
User login with authentication and session management.
Protected routes accessible only to logged-in users.
User logout functionality.
Project Structure
app.py: Main application file containing the Flask app setup and routes.
models.py: Defines the database model (Users) and FlaskForm classes (RegisterForm, LoginForm).
templates/: Directory containing HTML templates for different pages.
static/: Directory for static files such as stylesheets and images.
requirements.txt: List of project dependencies.
Dependencies
Flask
Flask-SQLAlchemy
Flask-Login
Flask-WTF
Flask-Bcrypt
Contributing
If you would like to contribute to this project, feel free to open an issue or submit a pull request.
