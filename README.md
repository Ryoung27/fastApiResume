# Resume API Project

This project is a microservices-based API built with FastAPI, MongoDB, and Docker, designed to serve resume data. Each service is responsible for a different section of the resume, such as personal info, experience, skills, and projects. This API is built to practice using FastAPI, Pydantic, and NoSQL databases within a microservices architecture.

## Table of Contents

- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Services](#services)
  - [Personal Info Service](#personal-info-service)
  - [Experience Service](#experience-service)
  - [Skills Service](#skills-service)
  - [Projects Service](#projects-service)
- [Environment Variables](#environment-variables)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Project Structure

```plaintext
resume_api_project/
│
├── docker-compose.yml          # Docker Compose configuration
├── mongo-init.js               # Initial data setup for MongoDB (optional)
│
├── personal_info_service/      # Microservice for Personal Information
│   ├── Dockerfile
│   ├── main.py
│   └── service/
│       ├── models.py
│       ├── database.py
│       └── personal_info_service.py
│
├── experience_service/         # Microservice for Work Experience
│   ├── Dockerfile
│   ├── main.py
│   └── service/
│       ├── models.py
│       ├── database.py
│       └── experience_service.py
│
├── skills_service/             # Microservice for Skills
│   ├── Dockerfile
│   ├── main.py
│   └── service/
│       ├── models.py
│       ├── database.py
│       └── skills_service.py
│
└── projects_service/           # Microservice for Projects
    ├── Dockerfile
    ├── main.py
    └── service/
        ├── models.py
        ├── database.py
        └── projects_service.py
```

Prerequisites
Docker
Docker Compose
Python 3.8+ and pip (if you wish to run any part of the project locally)
Installation
Clone the repository:

git clone https://github.com/YOUR_USERNAME/resume_api_project.git
cd resume_api_project
Ensure all necessary environment variables are set (e.g., MONGO_URI). You can define these variables in a .env file or directly within docker-compose.yml.

Build and start the services with Docker Compose:
docker-compose up --build
Usage
After starting Docker Compose, each service will be accessible on a unique port:

Personal Info Service: http://localhost:8001/personal-info
Experience Service: http://localhost:8002/experience
Skills Service: http://localhost:8003/skills
Projects Service: http://localhost:8004/projects
You can test these endpoints with any API client like Postman or using curl.

Services
Each microservice is designed to handle a specific section of the resume data.

Personal Info Service
Endpoint: /personal-info
Port: 8001
Function: Serves basic personal information such as name, contact details, and summary.
Experience Service
Endpoint: /experience
Port: 8002
Function: Serves professional experience data, detailing work history and responsibilities.
Skills Service
Endpoint: /skills
Port: 8003
Function: Serves skills data, organized by categories such as programming languages and frameworks.
Projects Service
Endpoint: /projects
Port: 8004
Function: Serves project information, showcasing portfolio or key accomplishments.
Environment Variables
Ensure the following environment variables are set:

MONGO_URI: The connection string for MongoDB. Example: mongodb://mongodb:27017.
These can be set directly in your shell or within docker-compose.yml.

Troubleshooting
Common Errors
Error: MongoDB Connection Refused
Ensure that MongoDB is properly configured and running in the Docker network.

Error: Cannot connect to microservice endpoint
Verify that each service is running on the correct port and accessible from your host machine.

Permission errors during installation
If you see permission errors while installing dependencies, try using pip install --user or running Docker with elevated privileges.

Debugging Tips
Check logs: Run docker-compose logs -f to view real-time logs for all services.
Service-specific logs: You can view logs for a specific service, e.g., docker-compose logs -f skills_service.
License
This project is licensed under the MIT License.

This `README.md` covers the setup, usage, and troubleshooting tips for the `resume_api_project`. Be sure to replace placeholder text, like the GitHub URL, with your actual information.
