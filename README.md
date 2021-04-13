# Online Book Store Project

The Online Book Store project is part of Advanced Database Systems class that implements the CRUD, and display functionalities of a SQL database (here SQlite3) through a web app.

Problem Statement:

You are asked to develop an e-commerce website for online book sale. It should provide the users with a catalog of different books available for purchase in the bookstore. A shopping cart should be provided to the users. The system should be implemented using a 3-tier approach.

In order to create an ecommerce website for online book sale, I used the Django framework (Python 3) to write the backend of the website.


The platforms utilised for this project are as follows: 
  - Django Web Framework
  - SQlite3 Database
  - HTML for formatting the text and implementing functional UI

# Features:
  - Display all books by category
  - Show all books present in the database
  - Add, Delete, Update books
  - List all books by a author
  - Flexible searching option based on publisher, title, and isbn 
  


# Prerequisites:
- Python3.x, pip, and python's venv module

# Building the project locally:
- Create a new venv virtual environment (recommmended method for developing to resolve version dependency issues) 
- ```pip install -r requirements.txt``` to install all the required python packages using pip


# Running the server:
- ```cd bookStore``` then run ```python3 manage.py runserver``` to start the server
- By default, you can find the webpage being served at ```localhost:8000``` but it can be configured in case it causes any issues for you. 

# Accessing Django Admin dashboard to update database.
Django admin dashboard can be accessed at ```localhost:8000/admin```.  To login follow steps below:

1) Create a superuser using the command '''python3 manage.py createsuperuser'''
2) Now you can log in via http://127.0.0.1:8000/admin page through which you can see the table created. You can modify them using the interface of superuser/admin.
Django admin dashboard can be accessed at ```localhost:8000/admin```. 

# Project Structure:
- bookApp application is present within the bookStore project and utilises most of the common components generated when setting up Django project for the firtst time. 
- queries.sql is included to show what some of the queries look like to populate the database
- HTML templates are present in the templates directory under the app's root folder. 

### ToDos

- [X] Design the ER diagram;
- [X] Books should be under different categories such as computer science, biology, novel, etc.
- [X] Write the commands for creating tables and inserting values;
- [X] Show the tables with the contents that you have inserted;
- [X] Add books, delete books, update books.
- [X] List all of the books for a given author;
- [X] Books are searchable via ISBN, title, author name, publisher, etc;
- [ ] Books can be added to a shoppinng cart; Can be checked out or saved;
- [X] Warehouse quantities need to be updated automatically; if there are only 5 books left in the warehouse, an alert should be trigged;
- [X] Give some statistics such as the top saled books, average saled book, etc.
- [ ] Implement shopping cart

