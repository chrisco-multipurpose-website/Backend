# Chrisco Church Backend Documentation
## Introduction
This project is a Flask-based web application designed to serve as a backend for a church management system. It provides various functionalities such as user authentication, managing church information, events, services, blogs, user profiles, comments, and more. The application utilizes Flask along with several extensions to handle different aspects like database management, JWT authentication, CORS support, and blueprint-based modularization.
## Project Setups

TO set up and run this project locally, follow these steps:
1. Clone the repository: Clone the project repository from [Github Repository URL]
2. Install Dependencies: Navigate to the project directory and install the required dependencies using pip: 
```python
pip install -r requirements.txt
```
3. Set Environment Variables: Create a .env file in the root directory of the project and define the following environment variables:
```python
SECRET_KEY=<your_secret_key>
DATABASE_URI=<your_database_uri>
```
4. Initialize Database: Run the following command to initialize the database and perform migrations:
```python
flask db init
flask db migrate
flask db upgrade
```
5. Run the Application: Start the Flask server by executing the following command:
```python
python app.py
```
6. Access the Application: Once the server is running, you can access the application by navigating to `http://localhost:5555` in your web browser.
## Project Flow
The project follows a modular structure where different components are organized into blueprints for better organization and maintainability. Here's a brief overview of the project flow:

- app.py: This is the main entry point of the application where Flask is initialized along with various extensions like Flask-Migrate, Flask-JWT-Extended, and Flask-CORS. It registers all the blueprints for different functionalities.

- **Blueprints:**
    - auth_bp: Handles user authentication and JWT token generation.
    - user_bp: Manages user-related functionalities such as registration, profile - updates, and user retrieval.
    - service_bp: Provides endpoints for managing church services.
    - churchinfo_bp: Manages church-related information.
    - event_bp: Handles church events.
    - about_bp: Manages information about the church.
    - department_bp: Handles church departments.
    - youtube_bp: Integrates with YouTube for church-related content.
    - spotify_bp: Integrates with Spotify for music-related content.
    - slider_bp: Manages sliders for displaying images or content.
    - blog_bp: Handles church blog posts.
    - profile_bp: Manages user profiles.
    - prayer_request_bp: Handles prayer requests.
    - comment_bp: Manages comments on different content.
    - inquiry_bp: Handles inquiries or messages.
    - subscription_bp: Manages subscriptions for receiving updates.

- **JWT Authentication:** JWT tokens are used for user authentication and authorization. Various JWT error handlers are implemented to handle expired tokens, invalid tokens, and unauthorized requests.

- **Database Models:** The application utilizes SQLAlchemy ORM to define and interact with database models. The User and TokenBlocklist models are used for managing user data and token revocation, respectively.

This setup allows for a scalable and modular architecture, making it easier to add new features and maintain existing ones.