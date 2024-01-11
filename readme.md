# Social Networking App API Documentation

Welcome to the Social Networking App API! This API allows you to build social networking features in your application, including user registration, authentication, friend requests, and more.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)


- [API Endpoints](#api-endpoints)
  - [1. User Registration](#1-user-registration)
  - [2. User Login](#2-user-login)
  - [3. Send Friend Request](#3-send-friend-request)
  - [4. Accept/Reject Friend Request](#4-accept-reject-friend-request)
  - [5. List Friends](#5-list-friends)
  - [6. Search Users](#6-search-users)
  - [7. Pending Friend Requests](#7-pending-friend-requests)



## Getting Started

### Prerequisites

- [Python](https://www.python.org/) (version 3.11)
- [Django](https://www.djangoproject.com/) (version 5.x)
- [Django Rest Framework](https://www.django-rest-framework.org/) (version 3.x)
- [PostgreSQL](https://www.postgresql.org/) (optional, for database storage)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/birajit95/Social-Netwokring-App.git

2. **Create  and activate the virtual Environment**

    ```bash
    python3.11 -m venv venv

    source venv/bin/activate

3. **Install Dependencies**
  - Go to project directory and run

    ```bash
    pip install -r requirements.txt

4. **Create .env file inside the project directory and place the below code**
    ```
      SECRET_KEY=django-insecure-rnqf4kft^qcqn+1-ur4d*$-$vh!s#mpznwjst5-b5fe7l^2l2v
      DB_NAME=accunox_db
      DB_USER=postgres
      DB_PASSWORD=postgres
      DB_HOST=localhost
    ```

    ***note:***
    - create a database in postgres sever named 'accunox_db'

5. **Create Migration Files and Migrate the Database**

    ```bash
        python manage.py makemigrations
        python manage.py migrate

6. **Start the Dev Server**
    ```
        python manage.py runserver
    ```



## API Endpoints

### 1. User Registration

- **Endpoint**: `/social-media/register/`
- **Method**: `POST`
- **Request Data**:
  - `username` (string, required): User's username.
  - `email` (string, required): User's email address.
  - `first_name` (string, required): User's password.
  - `last_name` (string, required): User's password.
  - `password` (string, required): User's password.
  - `confirm_password` (string, required): User's password.



### 2. User Login

- **Endpoint**: `/social-media/login/`
- **Method**: `POST`
- **Request Data**:
  - `emali` (string, required): User's username or email.
  - `password` (string, required): User's password.

### 3. Send Friend Request

- **Endpoint**: `/social-media/send-friend-request/`
- **Method**: `POST`
- **Request body**:
  - `requested_user_id` (integer, required): ID of the user to send the friend request.

### 4. Accept Reject Friend Request

- **Endpoint**: `/social-media/accept-or-reject-request//<request_id>/`
- **Method**: `PATCH`
- **Request Body**: 
   - `status` (string, required): Options: "accepted" / "rejected".

### 5. List Friends

- **Endpoint**: `/api/friends/`
- **Method**: `GET`
- **Parameters**: 
    - `page` (Integer, Optional): page number
    - `page_size` (Integer, Optional): page size

### 6. Search Users

- **Endpoint**: `/api/search-users/`
- **Method**: `GET`
- **Parameters**:
  - `search` (string, required): Search query for users.
  -  `page` (Integer, Optional): page number
  - `page_size` (Integer, Optional): page size



### 7. Pending Friend Requests

- **Endpoint**: `/api/pending-requests/`
- **Method**: `GET`
- **Parameters**:
    -  `page` (Integer, Optional): page number
    - `page_size` (Integer, Optional): page size



****
**Note**:
> I used rest_framewokr Token Authentication, so to call any api you need to pass token like below in request header

- Request Header
  - {
    "Authorization": "Token 397bf5a6be4a772882edf6a5931ee80e19652cc0"
  }






