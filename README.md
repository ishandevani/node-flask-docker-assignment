# Full-Stack Application Using Node.js, Express, Flask, and Docker

## Project Overview

This project demonstrates a containerized full-stack web application using Node.js, Express, and Flask. The frontend provides a user registration form, while the Flask backend validates and processes the submitted data.

Docker and Docker Compose are used to build, run, and connect the frontend and backend services. The Docker images are published to Docker Hub, and the source code is maintained in GitHub.

## Technologies Used

- Node.js
- Express.js
- Python
- Flask
- HTML and CSS
- Docker
- Docker Compose
- Docker Hub
- Git and GitHub

## Project Structure

```text
node-flask-docker-assignment/
├── frontend/
│   ├── public/
│   │   ├── index.html
│   │   └── style.css
│   ├── server.js
│   ├── package.json
│   ├── package-lock.json
│   ├── Dockerfile
│   └── .dockerignore
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .dockerignore
├── compose.yaml
├── .gitignore
└── README.md
```

## Application Features

- User registration form with Name, Age, and Email fields.
- Express server to serve frontend files.
- HTTP POST requests from the frontend to Express.
- Express forwards submissions to the Flask backend.
- Flask validates and processes the submitted information.
- JSON responses for successful and unsuccessful requests.
- Separate Docker images for frontend and backend.
- Docker Compose networking between services.
- Source code version control using GitHub.

## Run the Application

### Prerequisites

Install Docker Desktop or Docker Engine with the Docker Compose plugin.

### Start the services

```bash
docker compose build
docker compose up -d
```

### Access the application

- Frontend: http://localhost:3000
- Backend health check: http://localhost:5000/

### View logs

```bash
docker compose logs -f
```

### Stop the services

```bash
docker compose down
```

## Docker Hub

Published image repositories:

- Frontend: `YOUR_DOCKERHUB_USERNAME/fullstack-frontend:1.0`
- Backend: `YOUR_DOCKERHUB_USERNAME/fullstack-backend:1.0`

Replace the placeholder with your Docker Hub username.

## Testing

Submit the registration form through the frontend and verify that Flask returns a successful JSON response. Invalid inputs should return an appropriate error response.

## Learning Outcomes

This project demonstrates full-stack application development, REST API communication, containerization, service networking, image publishing, and source code management.

## Conclusion

The project integrates a Node.js and Express frontend with a Flask backend and uses Docker Compose to run both services as a connected application. Publishing the images to Docker Hub and maintaining the source code on GitHub demonstrates a basic containerized application deployment workflow.