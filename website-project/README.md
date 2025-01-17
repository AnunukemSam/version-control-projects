# **CI/CD Pipeline for Portfolio Website with Jenkins and GitHub Integration**

This comprehensive guide walks you through setting up a **CI/CD pipeline** for a portfolio website using **Jenkins**, **GitHub**, and a **web server** (e.g., Nginx or Apache2). We’ll also cover optional **Ngrok** usage for webhook testing.

---

## **Architectural Diagram**

![Architectural Diagram](https://raw.githubusercontent.com/AnunukemSam/version-control-projects/main/website-project/screenshots/CI_CD_Project.drawio.png)

## **Objective**

- Automate the building, testing, and deployment of a portfolio website.
- Use GitHub for version control and Jenkins for automation.
- Host the website on a web server such as Nginx or Apache2.

---

## **Directory Structure**

Organize your project files as follows:

```
project-root/
├── website/                   # Source code for the portfolio website
│   ├── index.html             # Homepage
│   ├── assets/                # Images, stylesheets, JavaScript files
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   └── README.md              # Website instructions
├── docs/                      # Documentation and resources
│   ├── pipeline-diagram.png   # CI/CD pipeline visualization
│   ├── webhook-setup.md       # GitHub webhook setup guide
│   └── other-documents/       # Additional resources
├── Jenkinsfile                # Jenkins pipeline configuration
├── .gitignore                 # Files to exclude from Git
```

### **Explanation**:
- **website/**: Houses the website's source code.
- **docs/**: Includes guides, screenshots, and diagrams.
- **Jenkinsfile**: Defines the Jenkins pipeline stages.
- **.gitignore**: Prevents unwanted files (e.g., `node_modules`, `.DS_Store`) from being tracked.

---

## **Prerequisites**

Ensure the following are set up on your system:

1. **Ubuntu VM** for Jenkins and the web server.
2. **GitHub repository** to store the website’s source code.
3. **Java Development Kit (JDK)**, version 17 or 21, installed on the VM.
4. **Git** installed on the VM.
5. **Ngrok** (optional) for exposing local services to the internet.

---

## **Detailed Steps**

---

### **Step 1: Install Jenkins on Ubuntu**

1. **Update your system**:
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

2. **Install Java**:
   - For JDK 17:
     ```bash
     sudo apt install openjdk-17-jdk -y
     ```
   - For JDK 21:
     ```bash
     sudo apt install openjdk-21-jdk -y
     ```

3. **Install Jenkins**:
   ```bash
   wget -q -O - https://pkg.jenkins.io/keys/jenkins.io.key | sudo apt-key add -
   echo "deb http://pkg.jenkins.io/debian/ stable main" | sudo tee /etc/apt/sources.list.d/jenkins.list
   sudo apt update
   sudo apt install jenkins -y
   ```

4. **Start and enable Jenkins**:
   ```bash
   sudo systemctl start jenkins
   sudo systemctl enable jenkins
   ```

5. **Access Jenkins**:
   - Open your browser and navigate to `http://<your-VM-IP>:8080`.
   - Retrieve the Jenkins unlock key:
     ```bash
     sudo cat /var/lib/jenkins/secrets/initialAdminPassword
     ```
   - Paste the key to unlock Jenkins and install the **recommended plugins**.

---

### **Step 2: Install and Configure Nginx**

1. **Install Nginx**:
   ```bash
   sudo apt install nginx -y
   ```

2. **Start and enable Nginx**:
   ```bash
   sudo systemctl start nginx
   sudo systemctl enable nginx
   ```

3. **Verify the setup**:
   Visit `http://<your-VM-IP>` in your browser to check if Nginx is running.

---

### **Step 3: Install Git**

1. **Install Git**:
   ```bash
   sudo apt install git -y
   ```

2. **Verify installation**:
   ```bash
   git --version
   ```

3. **Configure Git**:
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "youremail@example.com"
   ```

---

### **Step 4: Set Up GitHub Webhooks**

**Why Use Webhooks?**  
Webhooks allow GitHub to notify Jenkins about changes in the repository instantly, triggering automation workflows without delay.

#### **Steps to Set Up Webhooks**:
1. Navigate to your GitHub repository:
   - Go to **Settings** > **Webhooks** > **Add Webhook**.
2. Configure the webhook:
   - **Payload URL**: Use `http://<your-Jenkins-URL>:8080/github-webhook/` (or Ngrok for local testing).
   - **Content type**: `application/json`.
   - **Events**: Select **Just the push event**.
3. Save the webhook.

---

### **Step 5: Configure Git in Jenkins**
Now we need to configure GitHub credentials and ensure Git is available in Jenkins.

#### **Install Git in Jenkins**:

1. Go to Manage Jenkins > Global Tool Configuration.
    - Under Git, provide the path to the Git executable:
    - Run the following command on your VM to locate Git:
        ```bash
            which git
        ```
    Example output: /usr/bin/git.

2. Add GitHub Credentials:
    - Generate a Personal Access Token (PAT) from GitHub (for authentication):
    - Go to GitHub > Settings > Developer Settings > Personal Access Tokens > Generate new token.
    - Select the required scopes (e.g., repo, admin:repo_hook).
    - Save the token.
    
3. Add the token to Jenkins:
    - Go to Manage Jenkins > Manage Credentials > Global Credentials > Add Credentials.
    - Username: Your GitHub username.
    - Password: Paste your Personal Access Token (PAT).
    - Set ID as GitHub-PAT.

### **Step 6: Create and Configure a Jenkins Pipeline**

1. **Create a Pipeline Job**:
   - Log in to Jenkins and click **New Item**.
   - Select **Pipeline** and name it (e.g., "Portfolio Pipeline").

2. **Set Up the Pipeline**:
   - Under **Pipeline**, choose **Pipeline script from SCM**.
   - Select **Git** and enter your repository URL.
   - Add credentials (e.g., GitHub PAT).

---

### **Step 7: Write the Jenkinsfile**

Here’s a sample **Jenkinsfile**:

```groovy
pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout([$class: 'GitSCM', 
                              branches: [[name: '*/main']], 
                              userRemoteConfigs: [[
                                  url: 'https://github.com/yourusername/portfolio-website.git', 
                                  credentialsId: 'GitHub-PAT'
                              ]]])
                }
            }
        }
        stage('Build') {
            steps {
                echo 'Building the website...'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying website...'
                sh 'sudo cp -r * /var/www/html'
            }
        }
    }
}
```

#### **Pipeline Stages Explained**:
1. **Checkout**: Pulls the latest code from GitHub.
2. **Build**: Prepares the code (e.g., minifying CSS or JS).
3. **Test**: Verifies functionality and code quality.
4. **Deploy**: Deploys the code to the web server.

---

### **Step 8: Ngrok for Local Webhook Testing**

1. **Install Ngrok**:
   ```bash
   sudo snap install ngrok
   ```

2. **Expose Jenkins**:
   ```bash
   ngrok http 8080
   ```

3. **Update the webhook**:
   - Use the public URL provided by Ngrok (e.g., `http://<subdomain>.ngrok.io/github-webhook/`).

---

### **Step 9: Test the Pipeline**

1. **Push Changes to GitHub**:
   ```bash
   git add .
   git commit -m "Initial pipeline setup"
   git push origin main
   ```

2. **Monitor Jenkins**:
   - The pipeline should trigger automatically, building, testing, and deploying your portfolio website.

---

