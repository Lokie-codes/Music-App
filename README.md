# Music App

The Music App is a Django Rest Framework-based application that allows users to share music with others. \
It provides three types of access for the shared music: public, protected, and private. \
Users can sign up with their email and log in using their email and password. All files accessible by the user are visible to them. \
The application utilizes django-rest-auth for authentication and user registration.

## Routes

- User Registration: `POST` [http://127.0.0.1:8000/auth/register/](http://127.0.0.1:8000/auth/register/)
- User Login: `POST` [http://127.0.0.1:8000/auth/login/](http://127.0.0.1:8000/auth/login/)
- List of Accessible Music: `GET` [http://127.0.0.1:8000/api/music-list/](http://127.0.0.1:8000/api/music-list/)
- Add Music: `POST` [http://127.0.0.1:8000/api/music-list/](http://127.0.0.1:8000/api/music-list/)
- User Logout: `POST` [http://127.0.0.1:8000/auth/logout/](http://127.0.0.1:8000/auth/logout/)

## Features

1. **User Registration**: Users can create an account by providing their email and password. The registration endpoint accepts a `POST` request to `/auth/register/`. Successful registration returns the user details and a token for authentication.

2. **User Login**: Users can log in to the application using their email and password. The login endpoint accepts a `POST` request to `/auth/login/`. Successful login returns the user details and a token for authentication.

3. **List of Accessible Music**: Users can retrieve a list of music accessible to them. The endpoint accepts a `GET` request to `/api/music-list/` and returns a list of music files based on the user's access level (public, protected, or private).

4. **Add Music**: Users can upload music files to share with others. The endpoint accepts a `POST` request to `/api/music-list/` and requires the necessary information for the music file (e.g., file name, access level). Upon successful upload, the file becomes accessible based on the specified access level.

5. **User Logout**: Users can log out of the application, invalidating their authentication token. The logout endpoint accepts a `POST` request to `/auth/logout/` and logs the user out.

## User Authentication and Registration

The Music App utilizes django-rest-auth for user authentication and registration. Users are required to sign up with their email and password to create an account. They can then log in using their registered email and password. The authentication mechanism relies on tokens, which are returned upon successful registration and login. These tokens should be included in the request headers for subsequent authenticated requests.

## Testing

The Music App includes tests to ensure the application functions correctly. All test cases have been executed and passed successfully.

Feel free to explore the functionalities of the Music App and share your favorite music with others! If you encounter any issues or have any suggestions, please let us know.

---

## Getting Started

To get started with the Music App, follow these steps:

1. Clone the repository:
```
git clone 
```
Following instructions work on Linux OS environments.
2. Create Virtual Environment
```
python3 -m venv .env
```
3. Activate virtual environment
```
source .env/bin/activate
```
4. Install the project dependencies:
```
python -m pip install -r requirements.txt
```
5. Apply the database migrations:
```
python manage.py migrate
```
6. Run the development server:
```
python manage.py runserver
```
7. Access the application through your browser at `http://127.0.0.1:8000/`.

To gain administrative access, you can utilize the following command:
```
python manage.py createsuperuser
```
When prompted, you should enter the desired username, email address, and password for the admin account. This information will be used to create the superuser account with administrative privileges.
admin site can be accessed at `http://127.0.0.1:8000/admin/`

---
Enjoy using the Music App!