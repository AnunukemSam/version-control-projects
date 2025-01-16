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

# Portfolio Website Project Documentation

## Step 3: Setting Up the Portfolio Website Repository

### Objective:
Organize project files in a structured repository and prepare for collaborative development.

### Instructions:
1. **Create a Directory Structure:**
   - Inside your repository, create a folder named `ci-cd-portfolio-website`.
   - Within this folder, create two subdirectories:
     - `project` (for the website code).
     - `documentation` (for related project documentation).
   - Add a `README.md` file in the `ci-cd-portfolio-website` folder to document project details.

2. **Update the Repository:**
   - Add the directory structure to the repository.
   - Commit the changes with a clear commit message.

### Example Command:
```bash
mkdir -p ci-cd-portfolio-website/project ci-cd-portfolio-website/documentation
cd ci-cd-portfolio-website
nano README.md  # Add project details
```
Commit message:
```
feat: Add initial directory structure and README.md
```

---

## Step 4: Adding the Website Files

### Objective:
Develop and upload a basic, attractive portfolio website.

### Instructions:
1. **Download or Create Website Files:**
   - The website includes three main files:
     - `index.html`: Contains the structure and content of the website.
     - `style.css`: Defines the website's appearance.
     - `script.js`: Adds interactivity to the website.

2. **Place Files in the `project` Directory:**
   - Add the provided HTML, CSS, and JS files to the `project` directory.
   - Review the code to understand its functionality.

3. **Update the Repository:**
   - Commit the changes with a clear commit message.

### Example Command:
```bash
cd ci-cd-portfolio-website/project
# Add files here
```
Commit message:
```
feat: Add HTML, CSS, and JS files for the portfolio website
```

---

## Step 5: Testing the Portfolio Website Locally

### Objective:
Ensure the website functions as intended by testing it on a local server.

### Instructions:
1. **Start a Local HTTP Server:**
   - Navigate to the `project` directory in the terminal.
   - Run the following command to start a server:
     ```bash
     python3 -m http.server 8000
     ```
   - This starts a server accessible at `http://localhost:8000`.

2. **Open the Website in a Browser:**
   - Open a browser and enter the URL: `http://localhost:8000`.
   - Verify that the website loads correctly and appears as expected.

3. **Document Testing Results:**
   - Note any issues (e.g., broken links, alignment issues).
   - If no issues are found, document that testing was successful.

---

## Notes for Collaboration
1. **Commit Message Guidelines:**
   - Use clear and descriptive commit messages following this format:
     ```
     <type>: <short summary>

     <optional detailed description>
     ```
   - Example:
     ```
     feat: Add HTML, CSS, and JS files for the portfolio website

     Included a responsive design with interactivity using JavaScript.
     ```


---

