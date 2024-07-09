# Library Management RSETful API

## Overview

This project is a RESTful API for managing a library's inventory of books, authors. and users. It allows users to perform CRUD (Create, Read,Update, Delete) operations on these resources via HTTP requests. User authentication is implemented using JSON Web Tokens (JWT), ensuring secure access to protected endpoints.

### Key Features

-**Books**: Manage books including title, author, and user borrowing information.
-**Authors**: Manage authors including their information.
-**Users**: Register, login, and manage user information.
-**Authentication**: Secure API endpoints using JWT.
-**Error Handling**: Customer error handling for better API responses.

## Project Structure

The project follows a modular structure with separate components for models, services, resources (API endpoints), and utilities.

### Dependencies

Before running the application, ensure you have Python 3 and pip installed on your system. Install dependencies using:

```bash
pip install -r requirements.txt

