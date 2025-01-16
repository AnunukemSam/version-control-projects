# CI/CD Pipeline for Portfolio Website

This project demonstrates a basic CI/CD pipeline using Jenkins for automating the deployment of a portfolio website. It includes:
- A simple static portfolio website.
- Jenkins pipeline to test and deploy the website automatically.
- Best practices for CI/CD and security.

## Directory Structure
- `website/`: Contains the source code for the portfolio website.
- `docs/`: Documentation, screenshots, and diagrams.
- `Jenkinsfile`: The pipeline configuration for Jenkins.
- `.gitignore`: Lists files to exclude from version control.

---

### **Installing and Setting Up Jenkins**

**Purpose:**  
To automate CI/CD tasks, Jenkins is installed and configured on our local machines to integrate with the repository and perform build and deployment pipelines.

---

#### **Installation Steps:**

1. **For Windows (Host 1):**
   - Download the Jenkins installer from [Jenkins Downloads](https://www.jenkins.io/download/).
   - Run the installer and follow the setup instructions. Ensure Java 11 or 17 is installed if prompted.
   - After installation, open your browser and navigate to `http://localhost:8080`.
   - Retrieve the initial admin password from:  
     `C:\Program Files (x86)\Jenkins\secrets\initialAdminPassword`.
   - Paste the password in the browser prompt to unlock Jenkins.
   - Select "Install Suggested Plugins" and set up an admin user.

2. **For macOS (Host 2):**
   - Open the terminal and install Jenkins using Homebrew:  
     ```bash
     brew install jenkins-lts
     ```
   - Start Jenkins with:  
     ```bash
     brew services start jenkins-lts
     ```
   - Access Jenkins via `http://localhost:8080` in the browser.
   - Retrieve the initial admin password from:  
     `/Users/<username>/.jenkins/secrets/initialAdminPassword`.
   - Paste the password to unlock Jenkins.
   - Select "Install Suggested Plugins" and set up an admin user.

---

#### **Post-Installation Steps:**

1. **Install Git Plugin:**
   - Navigate to: **Manage Jenkins > Manage Plugins > Available Plugins**.
   - Search for **Git Plugin** and click "Install without restart."

2. **Configure Git in Jenkins:**
   - Go to **Manage Jenkins > Global Tool Configuration > Git**.
   - Ensure Jenkins detects Git. If not, provide the path to the Git executable:  
     - For Windows: Check `git --version` in Command Prompt to find the path.  
     - For macOS: Homebrew handles this automatically.

---

#### **Verification:**
- Open the browser and ensure Jenkins is running on `http://localhost:8080`.
- Confirm the Git plugin is installed and Jenkins can detect Git.

---

**Screenshots to Include:**
1. Jenkins welcome page (`http://localhost:8080`).
2. Admin password entry page.
3. Plugin installation progress.
4. Git configuration in **Global Tool Configuration**.

---

