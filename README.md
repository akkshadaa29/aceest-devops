# ACEest DevOps Assignment

## Overview

This project demonstrates a complete DevOps pipeline built around a simple Flask-based application.

The system includes:

* Flask API (basic endpoints)
* Unit testing using Pytest
* Docker containerization
* CI/CD using GitHub Actions
* Build automation using Jenkins

## Tech Stack

* Python (Flask)
* Pytest
* Docker
* GitHub Actions
* Jenkins

## Project Structure

aceest-devops/
│── app.py
│── test_app.py
│── requirements.txt
│── Dockerfile
│── .github/workflows/main.yml

## API Endpoints

The application currently includes two basic endpoints:

1. GET /clients
   Returns the list of clients

2. POST /clients
   Adds a new client (requires "name" field)

## Local Setup Instructions

### Clone Repository

git clone https://github.com/akkshadaa29/aceest-devops.git
cd aceest-devops

### Install Dependencies

python3 -m pip install -r requirements.txt

### Run Application

python3 app.py

### Access API

http://127.0.0.1:5000/clients

## Running Tests

pytest

## Docker Setup

### Build Image

docker build -t aceest-app .

### Run Container

docker run -p 5001:5000 aceest-app

### Access Application

http://127.0.0.1:5001/client

## CI/CD Pipeline (GitHub Actions)

The pipeline runs automatically on every push.

Steps:

1. Checkout code
2. Setup Python environment
3. Install dependencies
4. Run tests

## Jenkins Build

Jenkins is used as a secondary validation layer.

Steps:

1. Pull code from GitHub
2. Install dependencies
3. Run tests

Build command:

python3 -m pip install -r requirements.txt
pytest

## DevOps Pipeline Flow

Local Code → GitHub → GitHub Actions → Jenkins → Docker

## Conclusion

This project demonstrates a complete DevOps workflow including development, testing, integration, and deployment readiness.

## Author

Akshada Tambe
