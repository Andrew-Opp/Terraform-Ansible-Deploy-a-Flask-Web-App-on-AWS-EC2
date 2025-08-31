# Terraform + Ansible: Deploy a Flask Web App on AWS EC2

![Terraform](https://img.shields.io/badge/Terraform-IaC-623CE4?logo=terraform\&logoColor=white)
![Ansible](https://img.shields.io/badge/Ansible-Automation-EE0000?logo=ansible\&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-Cloud-232F3E?logo=amazonaws\&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python\&logoColor=white)

This project demonstrates a robust and automated workflow for deploying a simple web application on Amazon Web Services (AWS) using a combination of infrastructure as code (IaC) and configuration management tools. The workflow integrates Terraform, Ansible, and a Python script to provision the cloud infrastructure and deploy a basic Flask web application.

---

## 📂 Project Structure

```
terraform-ansible-flask-app/
├── terraform/
│   ├── main.tf                 # Terraform infrastructure definition
│   ├── outputs.tf              # Terraform outputs (EC2 IPs)
│   └── terraform_inventory.py  # Dynamic Ansible inventory script
├── ansible/
│   ├── playbook.yml            # Ansible playbook to configure EC2 + deploy app
├── .gitignore
└── README.md
```

---

## ⚙️ Prerequisites

* [Terraform](https://developer.hashicorp.com/terraform/downloads) installed
* [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) installed
* AWS CLI configured with proper credentials
* Python 3.8+ installed

---

## 🔑 Setup

1. **Clone this repository**

   ```bash
   git clone https://github.com/Andrew-Opp/Terraform-Ansible-Deploy-a-Flask-Web-App-on-AWS-EC2.git
   cd Terraform-Ansible-Deploy-a-Flask-Web-App-on-AWS-EC2
   ```

2. **Terraform: Initialize & Apply**

   ```bash
   cd terraform
   terraform init
   terraform apply -auto-approve
   ```

3. **Verify Terraform outputs**

   ```bash
   terraform output
   ```

4. **Add your SSH key (do not commit this file!)**
   Place your `web-key.pem` in the project root and restrict permissions:

   ```bash
   chmod 600 web-key.pem
   ```

---

## 🤖 Deploy with Ansible

1. **Run playbook**

   ```bash
   ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i terraform_inventory.py ../ansible/playbook.yml
   ```

---

## 🌐 Access the App

Once deployment is complete, visit:

```
http://<EC2-PUBLIC-IP>:8080
```

You should see:

```
Welcome to your App!
```

---

## 🏗️ Architecture Overview

```text
+-------------------------+
|       Developer         |
|  (Terraform + Ansible)  |
+-----------+-------------+
            |
            v
+-------------------------+
|     AWS Infrastructure  |
|  (Provisioned by IaC)   |
+-----------+-------------+
            |
            v
+-------------------------+
|      EC2 Instances      |
|  - Ubuntu + Flask App   |
|  - Configured by Ansible|
+-----------+-------------+
            |
            v
+-------------------------+
|   User Access via Web   |
|  http://<EC2-IP>:8080   |
+-------------------------+
```

---

## 🧹 Cleanup

To destroy all infrastructure:

```bash
cd terraform
tf destroy -auto-approve
```

---

## 📌 Notes

* `web-key.pem` and `*.tfstate` files are excluded via `.gitignore`.
* For production, consider using **Ansible roles** and **Terraform remote state**.
* Security group should allow inbound traffic on port **8080**.

---

## 📚 Learning Goals

✅ Learn Infrastructure as Code with Terraform
✅ Automate configuration with Ansible
✅ Use dynamic inventory with Terraform & Ansible
✅ Deploy a Python Flask app on AWS
