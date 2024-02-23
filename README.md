## Introduction

This is a simple Todo application built off Django (including the Django REST Framework for API CRUD operations) and React.

## Requirements
* Python3
* Pipenv

## Getting started
Navigate into the diretory ```[cd django-todo-react]```
Source the virtual environment ```[pipenv shell]```
pip install django-cors-headers
python -m pip install djangorestframework
Install the dependencies ```[pipenv install]```
Navigate into the frontend directory ```[cd frontend]```
Install the dependencies ```[npm install]```

## Run the application
You will need two terminals pointed to the frontend and backend directories to start the servers for this application.

1. Run this command to start the backend server in the ```[backend]``` directory: ```[python manage.py runserver]``` (You have to run this command while you are sourced into the virtual environment)
2. Run this command to start the frontend development server in the ```[frontend]``` directory: ```[npm install]``` (This will start the frontend on the adddress [localhost:3000](http://localhost:3000))
