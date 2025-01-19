# **DevOps Pipeline for Python App using Docker, Jenkins, Git, and Docker Compose**

## **Project Overview**

This project demonstrates the full implementation of a **DevOps pipeline** for a Python-based web application. The pipeline automates the following tasks:

- **Source Code Management (SCM)** using Git.
- **Continuous Integration (CI)** for automated testing with Jenkins.
- **Containerization** using Docker to package the app and its dependencies.
- **Multi-container orchestration** using Docker Compose for managing app and database containers.

The pipeline ensures seamless integration of all these tools, offering a complete DevOps workflow for your Python app.

---

## **Prerequisites**

Before starting, ensure that you have the following tools installed:

1. **Docker** - For containerizing your application.
   - [Docker Installation Guide](https://docs.docker.com/get-docker/)
2. **Docker Compose** - For managing multi-container applications.
   - [Docker Compose Installation Guide](https://docs.docker.com/compose/install/)
3. **Jenkins** - For automating the CI/CD pipeline.
   - [Jenkins Installation Guide](https://www.jenkins.io/doc/book/installing/)
4. **Git** - For version control.
   - [Git Installation Guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

---

## **Project Structure**

Here’s an overview of the project’s file structure:

```bash
.
├── Dockerfile
├── Jenkinsfile
├── docker-compose.yml
├── requirements.txt
├── app/
│   └── app.py
└── tests/
    └── test_app.py
```

- **Dockerfile**: Defines the steps for creating the Docker image for the Python app.
- **Jenkinsfile**: Defines the pipeline for Jenkins.
- **docker-compose.yml**: Defines the services, networks, and volumes for running multiple containers.
- **requirements.txt**: Lists the dependencies for the Python app.
- **app/**: Contains the Python web application code.
- **tests/**: Contains the unit tests for the Python app.

---

## **Step-by-Step Guide**

### **Step 1: Create the Python Web Application**

1. **Create the directory for the project:**

   ```bash
   mkdir devops-python-app
   cd devops-python-app
   ```

2. **Create the Python application file (`app.py`):**

   ```python
   # app/app.py
   from flask import Flask
   app = Flask(__name__)

   @app.route('/')
   def home():
       return "Welcome to the Search App!"

   if __name__ == "__main__":
       app.run(debug=True, host='0.0.0.0')
   ```

3. **Create a `requirements.txt` file to list the dependencies:**

   ```txt
   # requirements.txt
   flask
   pytest
   ```

---

### **Step 2: Dockerize the Application**

1. **Create a Dockerfile** to containerize the Python application:

   ```dockerfile
   # Dockerfile
   FROM python:3.8-slim

   WORKDIR /app
   COPY requirements.txt /app/
   RUN pip install --no-cache-dir -r requirements.txt
   COPY . /app/

   EXPOSE 5000

   CMD ["python", "app/app.py"]
   ```

2. **Build the Docker image:**

   ```bash
   docker build -t search-app .
   ```

3. **Run the Docker container:**

   ```bash
   docker run -d -p 5000:5000 search-app
   ```

   Your app should now be accessible at `http://localhost:5000`.

---

### **Step 3: Write Unit Tests**

1. **Create a directory for tests (`tests/test_app.py`):**

   ```python
   # tests/test_app.py
   import pytest
   from app.app import app

   @pytest.fixture
   def client():
       with app.test_client() as client:
           yield client

   def test_home(client):
       response = client.get('/')
       assert response.data == b'Welcome to the Search App!'
   ```

2. **Run the tests using `pytest`:**

   ```bash
   pytest
   ```

   Ensure that all tests pass before moving on.

---

### **Step 4: Set Up Jenkins Pipeline**

1. **Install Jenkins and set up your Jenkins server.**
   - Follow the installation guide from the Jenkins website.

2. **Create a new Pipeline project in Jenkins:**
   - In Jenkins, click on `New Item`, select `Pipeline`, and enter a project name.

3. **Create a Jenkinsfile** to define the pipeline:

   ```groovy
   # Jenkinsfile
   pipeline {
       agent any
       
       environment {
           DOCKER_IMAGE = "search-app"
       }
       
       stages {
           stage('Clone Repository') {
               steps {
                   checkout scm
               }
           }
           
           stage('Install Dependencies') {
               steps {
                   sh 'pip install -r requirements.txt'
               }
           }
           
           stage('Run Tests') {
               steps {
                   sh 'pytest'
               }
           }
           
           stage('Build Docker Image') {
               steps {
                   sh 'docker build -t $DOCKER_IMAGE .'
               }
           }
           
           stage('Run Docker Container') {
               steps {
                   sh 'docker run -d -p 5000:5000 $DOCKER_IMAGE'
               }
           }
       }
   }
   ```

4. **Push the `Jenkinsfile` to your Git repository:**

   ```bash
   git add Jenkinsfile
   git commit -m "Add Jenkinsfile for CI pipeline"
   git push origin main
   ```

---

### **Step 5: Docker Compose Setup**

1. **Create a `docker-compose.yml` file to manage multi-container services:**

   ```yaml
   # docker-compose.yml
   version: '3'
   services:
     app:
       build:
         context: .
         dockerfile: Dockerfile
       ports:
         - "5000:5000"
       depends_on:
         - db
       networks:
         - app-network

     db:
       image: postgres:latest
       environment:
         POSTGRES_USER: user
         POSTGRES_PASSWORD: password
         POSTGRES_DB: searchapp
       volumes:
         - db-data:/var/lib/postgresql/data
       networks:
         - app-network

   networks:
     app-network:
       driver: bridge

   volumes:
     db-data:
   ```

2. **Build and start the containers using Docker Compose:**

   ```bash
   docker-compose build
   docker-compose up -d
   ```

3. **Verify that both containers (app and db) are running:**

   ```bash
   docker-compose ps
   ```

4. **Access the app:**
   Open a browser and navigate to `http://localhost:5000`.

---

### **Step 6: Automate the Pipeline in Jenkins**

1. **In Jenkins, configure the pipeline job** to use your Git repository with the `Jenkinsfile` and the appropriate SCM settings.

2. **Run the Jenkins pipeline** and monitor the build. Jenkins will:
   - Pull the code from your Git repository.
   - Install dependencies.
   - Run unit tests.
   - Build the Docker image.
   - Deploy the app as a Docker container.

---

### **Step 7: Stopping and Cleaning Up**

1. **To stop and remove the containers using Docker Compose:**

   ```bash
   docker-compose down
   ```

2. **To remove all containers, networks, and volumes:**

   ```bash
   docker-compose down --volumes
   ```

---

## **Conclusion**

By following this README, you have successfully built and automated a **DevOps pipeline** for a Python web application using **Docker**, **Jenkins**, **Git**, and **Docker Compose**. You have learned how to:

- Dockerize a Python application.
- Automate CI/CD with Jenkins.
- Manage multi-container services using Docker Compose.
- Write unit tests and integrate them into the pipeline.

This pipeline is scalable and can be extended to include additional services, more advanced tests, and deployment to various environments.

---


