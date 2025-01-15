## **Web Server Ansible Setup Documentation**

## **Project Overview**
This project involves configuring a simple web server setup using Ansible, along with version control through Git. The goal is to automate the installation of Nginx on multiple web servers, as well as maintain infrastructure as code using Git and Ansible.

### **Use Case Scenario**
In a real-world scenario, you may have multiple web servers (either virtual machines or physical machines) that require consistent setup. Instead of manually configuring each server, you use Ansible to automate the setup, ensuring all your servers are consistently configured.

### **Architectural Diagram**
![Project Archtectural Diagram](https://raw.githubusercontent.com/AnunukemSam/version-control-projects/main/webserver-ansible-setup/screenshots/Version_Control_Web-Server_Setup_Architecture.drawio.png)

---

## **Prerequisites**
- **VM Setup**: We set up three Ubuntu server VMs: one as the **control node** (to run Ansible) and two as **managed nodes** (the web servers).
- **Git**: To keep track of changes in the project and playbooks.
- **Ansible**: To automate server configurations.
- **SSH Key-Based Authentication**: To enable password-less SSH login from the control node to managed nodes.

---

## **Step-by-Step Instructions**

### 1. **Setting up Version Control (Git)**

#### Clone your repository to the VM:

```bash
# Clone your repository (make sure you replace <your-github-repo-url>)
git clone <your-github-repo-url>
cd version-control-projects
```

#### Initialize the `webserver-ansible-setup` directory:

```bash
# Create a directory structure for the project
mkdir -p webserver-ansible-setup/files
mkdir -p webserver-ansible-setup/playbooks
mkdir -p webserver-ansible-setup/screenshots
cd webserver-ansible-setup
```

---

### 2. **Setting Up SSH Key-Based Authentication**

To enable password-less SSH login from the control node to the managed nodes, we need to generate an SSH key and copy it to the managed nodes.

#### Generate SSH Key on the Control Node:

```bash
# Generate SSH key pair on the control node
ssh-keygen -t rsa -b 2048
```

When prompted, just press Enter to save the key to the default location (i.e., `/home/username/.ssh/id_rsa`).

#### Copy the SSH Key to the Managed Nodes:

For each managed node, run the following command:

```bash
# Copy the SSH public key to the managed node
ssh-copy-id username@<managed-node-ip>
```

Replace `username` with the username on the managed node and `<managed-node-ip>` with the actual IP address of the managed node.

Once this is done, you should be able to SSH into the managed nodes without a password prompt.

#### Test SSH Connection:

```bash
# Test SSH connection to the managed node
ssh username@<managed-node-ip>
```

---

### 3. **Setting Up Ansible on the Control Node**

#### Install Ansible:

```bash
# On the control node, install Ansible (if not already installed)
sudo apt update
sudo apt install -y ansible
```

#### Create an `ansible` directory to store configurations:

```bash
# Create the Ansible configuration directory
sudo mkdir -p /etc/ansible
```

#### Create a hosts file to define your managed nodes:

```bash
# Edit the hosts file to add your managed nodes
sudo nano /etc/ansible/hosts
```

The `hosts` file should look like this, where `web_servers` is the group name for your web server VMs:

```
[web_servers]
192.168.1.10
192.168.1.11
```

Replace `192.168.1.10` and `192.168.1.11` with the actual IP addresses of your managed nodes.

---

### 4. **Creating the Ansible Playbook**

Create an Ansible playbook that will automate the setup of Nginx on the web servers:

```bash
# Create the playbook file in the playbooks directory
nano webserver-ansible-setup/playbooks/webserver-setup.yml
```

The playbook should look like this:

```yaml
---
- name: Configure web servers
  hosts: web_servers
  become: yes
  tasks:
    - name: Update package repository
      apt:
        update_cache: yes

    - name: Install Nginx
      apt:
        name: nginx
        state: latest

    - name: Start and enable webserver service
      service:
        name: nginx
        state: started
        enabled: yes

    - name: Copy HTML file to webserver document root
      copy:
        src: /home/username/version-control-projects/webserver-ansible-setup/files/index.html
        dest: /var/www/html/index.html
```

This playbook will:
1. Update the package repository on each web server.
2. Install Nginx if it's not already installed.
3. Start and enable the Nginx service to ensure it starts on boot.
4. Copy a simple `index.html` file to the web server's root directory.

---

### 5. **Create the HTML File**

```bash
# Create a simple HTML file that will be served by the web server in the files directory
nano webserver-ansible-setup/files/index.html
```

The HTML file can simply be:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Welcome to Nginx Web Server</title>
</head>
</html>
```

---

### 6. **Running the Ansible Playbook**

Now that the playbook is set up, run it from your control node to configure the web servers.

```bash
# Run the Ansible playbook to configure the web servers
cd webserver-setup.yml
ansible-playbook webserver-setup.yml --ask-become-pass
```

The `--ask-become-pass` flag will prompt for your password to escalate privileges (e.g., for installing packages).

---

### 7. **Git Commit and Push the Changes**

Once everything is set up, commit your changes and push them to your Git repository:

```bash
# Add changes to git
git add .

# Commit the changes
git commit -m "Configured web servers with Nginx via Ansible playbook"

# Push the changes to the repository
git push origin main
```

---

### 8. **Screenshot and Documentation**

![Playbook Output](https://raw.githubusercontent.com/AnunukemSam/version-control-projects/main/webserver-ansible-setup/screenshots/playbook_output.png)
*Above: The output after running the Ansible playbook.*

![Web Server Index](https://raw.githubusercontent.com/AnunukemSam/version-control-projects/main/webserver-ansible-setup/screenshots/webserver_index.png)
*Above: The web page served by Nginx after playbook execution.*
```

