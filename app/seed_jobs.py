from app.database import SessionLocal
from app.models import Job

jobs_data = [
    {
        "title": "AWS DevOps Engineer",
        "department": "Cloud & DevOps",
        "location": "Bengaluru, India",
        "employment_type": "Full Time",
        "experience": "0-2 Years",
        "description": "Work with AWS cloud infrastructure, CI/CD pipelines, automation and deployment.",
        "required_skills": "AWS, Docker, Kubernetes, Terraform, Jenkins, Git, Linux",
        "salary_range": "3-5 LPA"
    },
    {
        "title": "Azure DevOps Engineer",
        "department": "Cloud & DevOps",
        "location": "Hyderabad, India",
        "employment_type": "Full Time",
        "experience": "0-2 Years",
        "description": "Manage Azure cloud services, pipelines and infrastructure automation.",
        "required_skills": "Azure, Azure DevOps, Git, Docker, Kubernetes, Linux",
        "salary_range": "3-5 LPA"
    },
    {
        "title": "Cloud Engineer",
        "department": "Cloud Computing",
        "location": "Pune, India",
        "employment_type": "Full Time",
        "experience": "0-2 Years",
        "description": "Design, deploy and maintain cloud infrastructure.",
        "required_skills": "AWS, Azure, Networking, Linux, Docker",
        "salary_range": "3-5 LPA"
    },
    {
        "title": "Site Reliability Engineer",
        "department": "Cloud Operations",
        "location": "Bengaluru, India",
        "employment_type": "Full Time",
        "experience": "1-3 Years",
        "description": "Improve system reliability, monitoring and production operations.",
        "required_skills": "Linux, Kubernetes, Docker, Python, Prometheus, Grafana",
        "salary_range": "5-8 LPA"
    },
    {
        "title": "Kubernetes Engineer",
        "department": "Cloud & DevOps",
        "location": "Hyderabad, India",
        "employment_type": "Full Time",
        "experience": "1-3 Years",
        "description": "Manage Kubernetes clusters, deployments and container orchestration.",
        "required_skills": "Kubernetes, Docker, Helm, AWS, Linux",
        "salary_range": "4-7 LPA"
    },
    {
        "title": "Docker and Container Engineer",
        "department": "DevOps",
        "location": "Pune, India",
        "employment_type": "Full Time",
        "experience": "0-2 Years",
        "description": "Build and manage containerized applications and environments.",
        "required_skills": "Docker, Docker Compose, Kubernetes, Linux, Git",
        "salary_range": "3-5 LPA"
    },
    {
        "title": "CI/CD Pipeline Engineer",
        "department": "DevOps Automation",
        "location": "Bengaluru, India",
        "employment_type": "Full Time",
        "experience": "0-2 Years",
        "description": "Build and maintain automated build, testing and deployment pipelines.",
        "required_skills": "Jenkins, GitHub Actions, Git, Docker, Linux",
        "salary_range": "3-6 LPA"
    },
    {
        "title": "Infrastructure Automation Engineer",
        "department": "Infrastructure",
        "location": "Chennai, India",
        "employment_type": "Full Time",
        "experience": "1-3 Years",
        "description": "Automate infrastructure provisioning and configuration management.",
        "required_skills": "Terraform, Ansible, AWS, Python, Linux",
        "salary_range": "4-7 LPA"
    },
    {
        "title": "Terraform Engineer",
        "department": "Cloud Automation",
        "location": "Pune, India",
        "employment_type": "Full Time",
        "experience": "0-2 Years",
        "description": "Develop infrastructure as code using Terraform and cloud services.",
        "required_skills": "Terraform, AWS, Git, Linux, CI/CD",
        "salary_range": "3-5 LPA"
    },
    {
        "title": "DevSecOps Engineer",
        "department": "Cloud Security",
        "location": "Bengaluru, India",
        "employment_type": "Full Time",
        "experience": "1-3 Years",
        "description": "Integrate security practices into development and deployment pipelines.",
        "required_skills": "AWS, Docker, Kubernetes, Jenkins, Security Scanning",
        "salary_range": "5-8 LPA"
    },
    {
        "title": "Linux System Engineer",
        "department": "IT Infrastructure",
        "location": "Hyderabad, India",
        "employment_type": "Full Time",
        "experience": "0-2 Years",
        "description": "Manage Linux servers, system administration and troubleshooting.",
        "required_skills": "Linux, Shell Scripting, Networking, AWS, Python",
        "salary_range": "3-5 LPA"
    },
        {
        "title": "AWS Cloud Architect",
        "department": "Cloud Architecture",
        "location": "Bengaluru, India",
        "employment_type": "Full Time",
        "experience": "3-5 Years",
        "description": "Design scalable, secure and highly available AWS cloud architectures.",
        "required_skills": "AWS, VPC, EC2, S3, IAM, CloudFormation, Terraform",
        "salary_range": "8-14 LPA"
    },
    {
        "title": "AWS Infrastructure Engineer",
        "department": "Cloud Infrastructure",
        "location": "Pune, India",
        "employment_type": "Full Time",
        "experience": "1-3 Years",
        "description": "Build and maintain AWS infrastructure and automate cloud operations.",
        "required_skills": "AWS, EC2, VPC, IAM, Terraform, Linux",
        "salary_range": "4-8 LPA"
    },
    {
        "title": "AWS Solutions Engineer",
        "department": "Cloud Solutions",
        "location": "Hyderabad, India",
        "employment_type": "Full Time",
        "experience": "1-3 Years",
        "description": "Implement cloud solutions and support application migration to AWS.",
        "required_skills": "AWS, S3, RDS, EC2, Lambda, Networking",
        "salary_range": "5-9 LPA"
    },
    {
        "title": "AWS Cloud Support Associate",
        "department": "Cloud Support",
        "location": "Chennai, India",
        "employment_type": "Full Time",
        "experience": "0-1 Years",
        "description": "Monitor AWS services and troubleshoot cloud infrastructure issues.",
        "required_skills": "AWS, EC2, S3, IAM, Linux, Networking",
        "salary_range": "3-5 LPA"
    },
    {
        "title": "Azure Cloud Administrator",
        "department": "Cloud Operations",
        "location": "Bengaluru, India",
        "employment_type": "Full Time",
        "experience": "1-3 Years",
        "description": "Administer Azure resources, virtual machines and cloud networking.",
        "required_skills": "Azure, Virtual Machines, Azure Storage, Networking, PowerShell",
        "salary_range": "4-7 LPA"
    },
    {
        "title": "Azure Infrastructure Engineer",
        "department": "Cloud Infrastructure",
        "location": "Pune, India",
        "employment_type": "Full Time",
        "experience": "1-3 Years",
        "description": "Manage Azure infrastructure and automate cloud deployments.",
        "required_skills": "Azure, Terraform, ARM Templates, Linux, Git",
        "salary_range": "5-8 LPA"
    },
    {
        "title": "Kubernetes Administrator",
        "department": "Container Operations",
        "location": "Chennai, India",
        "employment_type": "Full Time",
        "experience": "1-3 Years",
        "description": "Administer Kubernetes clusters and manage container workloads.",
        "required_skills": "Kubernetes, Docker, Helm, Linux, Networking",
        "salary_range": "5-8 LPA"
    },
    {
        "title": "Amazon EKS Engineer",
        "department": "Cloud & DevOps",
        "location": "Bengaluru, India",
        "employment_type": "Full Time",
        "experience": "1-3 Years",
        "description": "Deploy and manage containerized applications using Amazon EKS.",
        "required_skills": "AWS EKS, Kubernetes, Docker, IAM, Terraform",
        "salary_range": "5-9 LPA"
    },
    {
        "title": "Container Platform Engineer",
        "department": "Platform Engineering",
        "location": "Hyderabad, India",
        "employment_type": "Full Time",
        "experience": "2-4 Years",
        "description": "Develop and maintain enterprise container platforms.",
        "required_skills": "Docker, Kubernetes, Helm, Linux, Jenkins",
        "salary_range": "6-10 LPA"
    },
    {
        "title": "Jenkins Automation Engineer",
        "department": "DevOps Automation",
        "location": "Pune, India",
        "employment_type": "Full Time",
        "experience": "1-3 Years",
        "description": "Develop Jenkins pipelines and automate software delivery workflows.",
        "required_skills": "Jenkins, Groovy, Git, Docker, Linux",
        "salary_range": "4-7 LPA"
    },
    {
        "title": "GitHub Actions Engineer",
        "department": "CI/CD Engineering",
        "location": "Bengaluru, India",
        "employment_type": "Full Time",
        "experience": "0-2 Years",
        "description": "Create automated CI/CD workflows using GitHub Actions.",
        "required_skills": "GitHub Actions, Git, YAML, Docker, AWS",
        "salary_range": "3-6 LPA"
    },
    {
        "title": "Release Automation Engineer",
        "department": "Release Engineering",
        "location": "Chennai, India",
        "employment_type": "Full Time",
        "experience": "1-3 Years",
        "description": "Manage software releases and automate deployment processes.",
        "required_skills": "Jenkins, Git, CI/CD, Docker, Linux",
        "salary_range": "4-7 LPA"
    },
    {
        "title": "Ansible Automation Engineer",
        "department": "Infrastructure Automation",
        "location": "Hyderabad, India",
        "employment_type": "Full Time",
        "experience": "1-3 Years",
        "description": "Automate server configuration and infrastructure management.",
        "required_skills": "Ansible, Linux, Python, YAML, AWS",
        "salary_range": "4-7 LPA"
    },
    {
        "title": "Infrastructure as Code Engineer",
        "department": "Cloud Automation",
        "location": "Bengaluru, India",
        "employment_type": "Full Time",
        "experience": "2-4 Years",
        "description": "Develop reusable infrastructure automation modules.",
        "required_skills": "Terraform, AWS, Ansible, Git, Python",
        "salary_range": "6-10 LPA"
    },
    {
        "title": "Platform Engineer",
        "department": "Platform Engineering",
        "location": "Pune, India",
        "employment_type": "Full Time",
        "experience": "2-4 Years",
        "description": "Build internal developer platforms and deployment automation tools.",
        "required_skills": "Kubernetes, Docker, Terraform, AWS, Python",
        "salary_range": "6-11 LPA"
    },
    {
        "title": "DevOps Build Engineer",
        "department": "Build Engineering",
        "location": "Chennai, India",
        "employment_type": "Full Time",
        "experience": "0-2 Years",
        "description": "Manage build automation, artifact repositories and deployment pipelines.",
        "required_skills": "Jenkins, Maven, Git, Docker, Linux",
        "salary_range": "3-6 LPA"
    },
    {
        "title": "Cloud Security Engineer",
        "department": "Cloud Security",
        "location": "Bengaluru, India",
        "employment_type": "Full Time",
        "experience": "2-4 Years",
        "description": "Implement cloud security controls and monitor infrastructure risks.",
        "required_skills": "AWS, IAM, Security, Networking, Linux",
        "salary_range": "6-11 LPA"
    },
    {
        "title": "DevSecOps Automation Engineer",
        "department": "Security Engineering",
        "location": "Hyderabad, India",
        "employment_type": "Full Time",
        "experience": "1-3 Years",
        "description": "Integrate security scanning and compliance checks into CI/CD pipelines.",
        "required_skills": "Jenkins, Docker, Kubernetes, SAST, DAST, AWS",
        "salary_range": "5-9 LPA"
    },
    {
        "title": "Cloud Monitoring Engineer",
        "department": "Cloud Operations",
        "location": "Pune, India",
        "employment_type": "Full Time",
        "experience": "1-3 Years",
        "description": "Monitor cloud infrastructure performance and system availability.",
        "required_skills": "Prometheus, Grafana, CloudWatch, AWS, Linux",
        "salary_range": "4-7 LPA"
    },
    {
        "title": "Observability Engineer",
        "department": "Site Reliability",
        "location": "Bengaluru, India",
        "employment_type": "Full Time",
        "experience": "2-4 Years",
        "description": "Build monitoring, logging and distributed tracing solutions.",
        "required_skills": "Grafana, Prometheus, ELK, Kubernetes, Linux",
        "salary_range": "6-10 LPA"
    },
    {
        "title": "Linux DevOps Administrator",
        "department": "IT Operations",
        "location": "Hyderabad, India",
        "employment_type": "Full Time",
        "experience": "0-2 Years",
        "description": "Manage Linux environments, shell scripts and server operations.",
        "required_skills": "Linux, Bash, Shell Scripting, Python, Networking",
        "salary_range": "3-6 LPA"
    },
    {
        "title": "Production Support Engineer",
        "department": "Production Operations",
        "location": "Chennai, India",
        "employment_type": "Full Time",
        "experience": "0-2 Years",
        "description": "Monitor production applications and troubleshoot operational incidents.",
        "required_skills": "Linux, SQL, AWS, Monitoring, Networking",
        "salary_range": "3-6 LPA"
    },
    {
        "title": "Cloud Migration Engineer",
        "department": "Cloud Transformation",
        "location": "Pune, India",
        "employment_type": "Full Time",
        "experience": "2-4 Years",
        "description": "Support migration of applications and infrastructure to cloud platforms.",
        "required_skills": "AWS, Azure, Networking, Linux, Terraform",
        "salary_range": "6-10 LPA"
    },
    {
        "title": "Multi Cloud Engineer",
        "department": "Cloud Engineering",
        "location": "Bengaluru, India",
        "employment_type": "Full Time",
        "experience": "2-4 Years",
        "description": "Manage workloads and infrastructure across multiple cloud platforms.",
        "required_skills": "AWS, Azure, Kubernetes, Terraform, Linux",
        "salary_range": "6-11 LPA"
    },
    {
        "title": "DevOps Engineer - Fresher",
        "department": "Cloud & DevOps",
        "location": "Mysuru, India",
        "employment_type": "Full Time",
        "experience": "Fresher",
        "description": "Entry-level opportunity to learn cloud infrastructure, automation and deployment.",
        "required_skills": "AWS, Linux, Git, Docker, Jenkins, Python",
        "salary_range": "2.5-4 LPA"
    },
        {
        "title": "Senior AWS DevOps Engineer",
        "department": "Cloud & DevOps",
        "location": "Bengaluru, India",
        "employment_type": "Full Time",
        "experience": "4-6 Years",
        "description": "Design and manage enterprise AWS DevOps infrastructure.",
        "required_skills": "AWS, Jenkins, Docker, Kubernetes, Terraform, Python",
        "salary_range": "10-18 LPA"
    },
    {
        "title": "Junior DevOps Engineer",
        "department": "DevOps",
        "location": "Pune, India",
        "employment_type": "Full Time",
        "experience": "0-1 Years",
        "description": "Support CI/CD pipelines and cloud deployment activities.",
        "required_skills": "Linux, Git, Docker, AWS, Jenkins",
        "salary_range": "3-5 LPA"
    },
    {
        "title": "AWS Lambda Developer",
        "department": "Serverless Computing",
        "location": "Hyderabad, India",
        "employment_type": "Full Time",
        "experience": "1-3 Years",
        "description": "Develop serverless applications using AWS Lambda.",
        "required_skills": "AWS Lambda, Python, API Gateway, DynamoDB, S3",
        "salary_range": "5-9 LPA"
    },
    {
        "title": "AWS Database Administrator",
        "department": "Cloud Database",
        "location": "Chennai, India",
        "employment_type": "Full Time",
        "experience": "2-4 Years",
        "description": "Manage cloud databases and database performance.",
        "required_skills": "AWS RDS, PostgreSQL, MySQL, SQL, AWS",
        "salary_range": "5-9 LPA"
    },
    {
        "title": "AWS Networking Engineer",
        "department": "Cloud Networking",
        "location": "Bengaluru, India",
        "employment_type": "Full Time",
        "experience": "2-4 Years",
        "description": "Configure and troubleshoot AWS networking infrastructure.",
        "required_skills": "AWS VPC, Subnets, NAT Gateway, Route Tables, DNS",
        "salary_range": "6-10 LPA"
    },
    {
        "title": "AWS Cloud Operations Engineer",
        "department": "Cloud Operations",
        "location": "Pune, India",
        "employment_type": "Full Time",
        "experience": "1-3 Years",
        "description": "Maintain cloud infrastructure and monitor AWS resources.",
        "required_skills": "AWS, EC2, CloudWatch, IAM, Linux",
        "salary_range": "4-8 LPA"
    },
    {
        "title": "AWS DevOps Trainee",
        "department": "Cloud & DevOps",
        "location": "Mysuru, India",
        "employment_type": "Full Time",
        "experience": "Fresher",
        "description": "Learn AWS cloud services and DevOps automation practices.",
        "required_skills": "AWS, Linux, Git, Python, Docker",
        "salary_range": "2.5-4 LPA"
    },
    {
        "title": "AWS Migration Specialist",
        "department": "Cloud Migration",
        "location": "Hyderabad, India",
        "employment_type": "Full Time",
        "experience": "3-5 Years",
        "description": "Plan and execute infrastructure migration to AWS.",
        "required_skills": "AWS, EC2, S3, VPC, Migration Hub, Linux",
        "salary_range": "8-13 LPA"
    },
    {
        "title": "AWS Cloud Consultant",
        "department": "Cloud Consulting",
        "location": "Bengaluru, India",
        "employment_type": "Full Time",
        "experience": "2-4 Years",
        "description": "Provide cloud architecture and implementation guidance.",
        "required_skills": "AWS, Cloud Architecture, Terraform, Networking, Security",
        "salary_range": "7-12 LPA"
    },
    {
        "title": "AWS Infrastructure Support Engineer",
        "department": "Technical Support",
        "location": "Chennai, India",
        "employment_type": "Full Time",
        "experience": "0-2 Years",
        "description": "Troubleshoot AWS infrastructure and application issues.",
        "required_skills": "AWS, EC2, S3, IAM, Linux, Troubleshooting",
        "salary_range": "3-6 LPA"
    },
    {
        "title": "Azure DevOps Specialist",
        "department": "Azure Engineering",
        "location": "Bengaluru, India",
        "employment_type": "Full Time",
        "experience": "2-4 Years",
        "description": "Build automated deployment pipelines using Azure DevOps.",
        "required_skills": "Azure DevOps, YAML, Git, Docker, Kubernetes",
        "salary_range": "6-10 LPA"
    },
    {
        "title": "Azure Kubernetes Engineer",
        "department": "Container Engineering",
        "location": "Hyderabad, India",
        "employment_type": "Full Time",
        "experience": "2-4 Years",
        "description": "Deploy and manage container applications using AKS.",
        "required_skills": "Azure AKS, Kubernetes, Docker, Helm, Terraform",
        "salary_range": "6-11 LPA"
    },
    {
        "title": "Azure Cloud Support Engineer",
        "department": "Cloud Support",
        "location": "Pune, India",
        "employment_type": "Full Time",
        "experience": "0-2 Years",
        "description": "Provide technical support for Microsoft Azure services.",
        "required_skills": "Azure, Virtual Machines, Networking, Linux, PowerShell",
        "salary_range": "3-6 LPA"
    },
    {
        "title": "Azure Infrastructure Administrator",
        "department": "Infrastructure",
        "location": "Chennai, India",
        "employment_type": "Full Time",
        "experience": "1-3 Years",
        "description": "Manage Azure virtual machines and cloud infrastructure.",
        "required_skills": "Azure, Networking, PowerShell, Windows Server, Linux",
        "salary_range": "4-8 LPA"
    },
    {
        "title": "Multi Cloud DevOps Engineer",
        "department": "Cloud Engineering",
        "location": "Pune, India",
        "employment_type": "Full Time",
        "experience": "3-5 Years",
        "description": "Implement automation across multiple cloud environments.",
        "required_skills": "AWS, Azure, Terraform, Docker, Kubernetes, Jenkins",
        "salary_range": "8-14 LPA"
    },
    {
        "title": "Google Cloud Engineer",
        "department": "Cloud Infrastructure",
        "location": "Bengaluru, India",
        "employment_type": "Full Time",
        "experience": "1-3 Years",
        "description": "Manage Google Cloud infrastructure and deployments.",
        "required_skills": "GCP, Compute Engine, Kubernetes, Terraform, Linux",
        "salary_range": "5-9 LPA"
    },
    {
        "title": "Google Kubernetes Engine Engineer",
        "department": "Container Platform",
        "location": "Hyderabad, India",
        "employment_type": "Full Time",
        "experience": "2-4 Years",
        "description": "Manage containerized workloads on Google Kubernetes Engine.",
        "required_skills": "GKE, Kubernetes, Docker, Helm, GCP",
        "salary_range": "6-11 LPA"
    },
    {
        "title": "Cloud Platform Administrator",
        "department": "Cloud Operations",
        "location": "Chennai, India",
        "employment_type": "Full Time",
        "experience": "1-3 Years",
        "description": "Administer cloud platforms and manage infrastructure resources.",
        "required_skills": "AWS, Azure, Linux, Networking, IAM",
        "salary_range": "4-8 LPA"
    },
    {
        "title": "Cloud Infrastructure Architect",
        "department": "Cloud Architecture",
        "location": "Pune, India",
        "employment_type": "Full Time",
        "experience": "5-7 Years",
        "description": "Design secure and scalable cloud infrastructure solutions.",
        "required_skills": "AWS, Azure, Terraform, Kubernetes, Cloud Security",
        "salary_range": "12-20 LPA"
    },
    {
        "title": "DevOps Intern",
        "department": "DevOps",
        "location": "Mysuru, India",
        "employment_type": "Internship",
        "experience": "Fresher",
        "description": "Assist with cloud deployments and automation projects.",
        "required_skills": "Linux, Git, AWS, Docker, Python",
        "salary_range": "10,000-20,000 per month"
    },
    {
        "title": "Kubernetes DevOps Specialist",
        "department": "Container Engineering",
        "location": "Bengaluru, India",
        "employment_type": "Full Time",
        "experience": "3-5 Years",
        "description": "Build and maintain Kubernetes-based deployment environments.",
        "required_skills": "Kubernetes, Docker, Helm, Jenkins, AWS",
        "salary_range": "8-13 LPA"
    },
    {
        "title": "Docker Platform Engineer",
        "department": "Platform Engineering",
        "location": "Pune, India",
        "employment_type": "Full Time",
        "experience": "2-4 Years",
        "description": "Manage Docker environments and container deployment workflows.",
        "required_skills": "Docker, Docker Compose, Kubernetes, Linux, Git",
        "salary_range": "5-9 LPA"
    },
    {
        "title": "Helm Chart Engineer",
        "department": "Kubernetes Engineering",
        "location": "Hyderabad, India",
        "employment_type": "Full Time",
        "experience": "2-4 Years",
        "description": "Create and maintain Helm charts for Kubernetes applications.",
        "required_skills": "Helm, Kubernetes, Docker, YAML, AWS",
        "salary_range": "5-9 LPA"
    },
    {
        "title": "EKS Platform Administrator",
        "department": "Cloud Platform",
        "location": "Chennai, India",
        "employment_type": "Full Time",
        "experience": "2-4 Years",
        "description": "Operate Amazon EKS clusters and manage platform reliability.",
        "required_skills": "AWS EKS, Kubernetes, IAM, Linux, Terraform",
        "salary_range": "6-10 LPA"
    },
    {
        "title": "Container Security Engineer",
        "department": "Cloud Security",
        "location": "Bengaluru, India",
        "employment_type": "Full Time",
        "experience": "2-4 Years",
        "description": "Secure container images and Kubernetes workloads.",
        "required_skills": "Docker, Kubernetes, Trivy, AWS, Linux",
        "salary_range": "6-11 LPA"
    },
    {
        "title": "Jenkins Pipeline Developer",
        "department": "CI/CD Engineering",
        "location": "Pune, India",
        "employment_type": "Full Time",
        "experience": "1-3 Years",
        "description": "Develop and maintain automated Jenkins pipelines.",
        "required_skills": "Jenkins, Groovy, Git, Maven, Docker",
        "salary_range": "4-8 LPA"
    },
    {
        "title": "CI/CD Automation Specialist",
        "department": "Release Automation",
        "location": "Hyderabad, India",
        "employment_type": "Full Time",
        "experience": "2-4 Years",
        "description": "Automate build, testing and deployment workflows.",
        "required_skills": "Jenkins, GitHub Actions, GitLab CI, Docker, Linux",
        "salary_range": "5-9 LPA"
    },
    {
        "title": "GitLab CI/CD Engineer",
        "department": "DevOps Automation",
        "location": "Chennai, India",
        "employment_type": "Full Time",
        "experience": "1-3 Years",
        "description": "Implement continuous integration pipelines using GitLab.",
        "required_skills": "GitLab CI, Git, Docker, Kubernetes, YAML",
        "salary_range": "4-8 LPA"
    },
    {
        "title": "Build and Release Engineer",
        "department": "Release Engineering",
        "location": "Bengaluru, India",
        "employment_type": "Full Time",
        "experience": "2-4 Years",
        "description": "Manage software build systems and release automation.",
        "required_skills": "Jenkins, Maven, Git, Linux, Docker",
        "salary_range": "5-9 LPA"
    },
    {
        "title": "DevOps Tools Engineer",
        "department": "DevOps Engineering",
        "location": "Pune, India",
        "employment_type": "Full Time",
        "experience": "2-4 Years",
        "description": "Maintain and integrate tools used across DevOps workflows.",
        "required_skills": "Jenkins, Git, Docker, Terraform, Ansible",
        "salary_range": "5-9 LPA"
    },
    {
        "title": "Terraform Cloud Engineer",
        "department": "Infrastructure Automation",
        "location": "Hyderabad, India",
        "employment_type": "Full Time",
        "experience": "2-4 Years",
        "description": "Build reusable Terraform modules for cloud infrastructure.",
        "required_skills": "Terraform, AWS, Azure, HCL, Git",
        "salary_range": "6-10 LPA"
    },
    {
        "title": "Ansible Configuration Engineer",
        "department": "Configuration Management",
        "location": "Bengaluru, India",
        "employment_type": "Full Time",
        "experience": "1-3 Years",
        "description": "Automate server configuration and application deployment.",
        "required_skills": "Ansible, Linux, Python, YAML, AWS",
        "salary_range": "4-8 LPA"
    },
    {
        "title": "Python Automation Engineer",
        "department": "Automation Engineering",
        "location": "Chennai, India",
        "employment_type": "Full Time",
        "experience": "1-3 Years",
        "description": "Develop Python scripts to automate infrastructure operations.",
        "required_skills": "Python, Linux, AWS, REST API, Git",
        "salary_range": "4-8 LPA"
    },
    {
        "title": "Infrastructure Automation Trainee",
        "department": "Cloud Automation",
        "location": "Mysuru, India",
        "employment_type": "Full Time",
        "experience": "Fresher",
        "description": "Assist in automating cloud infrastructure and server configuration.",
        "required_skills": "Linux, Python, Git, AWS, Ansible",
        "salary_range": "2.5-4 LPA"
    },
    {
        "title": "Site Reliability Engineer - Junior",
        "department": "Site Reliability Engineering",
        "location": "Pune, India",
        "employment_type": "Full Time",
        "experience": "0-2 Years",
        "description": "Support system availability and production monitoring.",
        "required_skills": "Linux, Python, AWS, Docker, Monitoring",
        "salary_range": "4-7 LPA"
    },
    {
        "title": "Senior Site Reliability Engineer",
        "department": "Site Reliability Engineering",
        "location": "Bengaluru, India",
        "employment_type": "Full Time",
        "experience": "4-6 Years",
        "description": "Improve production reliability and automate operational processes.",
        "required_skills": "Kubernetes, AWS, Prometheus, Grafana, Python",
        "salary_range": "10-16 LPA"
    },
    {
        "title": "Production Reliability Engineer",
        "department": "Production Engineering",
        "location": "Hyderabad, India",
        "employment_type": "Full Time",
        "experience": "2-4 Years",
        "description": "Improve application reliability and troubleshoot production incidents.",
        "required_skills": "Linux, AWS, Kubernetes, Monitoring, Python",
        "salary_range": "6-10 LPA"
    },
    {
        "title": "Prometheus Monitoring Engineer",
        "department": "Monitoring & Observability",
        "location": "Chennai, India",
        "employment_type": "Full Time",
        "experience": "1-3 Years",
        "description": "Implement metrics collection and monitoring dashboards.",
        "required_skills": "Prometheus, Grafana, Linux, Kubernetes, AWS",
        "salary_range": "4-8 LPA"
    },
    {
        "title": "Grafana Dashboard Engineer",
        "department": "Monitoring & Observability",
        "location": "Pune, India",
        "employment_type": "Full Time",
        "experience": "1-3 Years",
        "description": "Develop dashboards for infrastructure and application monitoring.",
        "required_skills": "Grafana, Prometheus, SQL, Linux, CloudWatch",
        "salary_range": "4-8 LPA"
    },
    {
        "title": "ELK Stack Engineer",
        "department": "Logging & Monitoring",
        "location": "Bengaluru, India",
        "employment_type": "Full Time",
        "experience": "2-4 Years",
        "description": "Build centralized logging and log analytics solutions.",
        "required_skills": "Elasticsearch, Logstash, Kibana, Linux, AWS",
        "salary_range": "5-9 LPA"
    },
    {
        "title": "Cloud Security Analyst",
        "department": "Information Security",
        "location": "Hyderabad, India",
        "employment_type": "Full Time",
        "experience": "1-3 Years",
        "description": "Monitor cloud security events and investigate infrastructure risks.",
        "required_skills": "AWS IAM, Cloud Security, Linux, Networking, SIEM",
        "salary_range": "4-8 LPA"
    },
    {
        "title": "Infrastructure Security Engineer",
        "department": "Infrastructure Security",
        "location": "Chennai, India",
        "employment_type": "Full Time",
        "experience": "3-5 Years",
        "description": "Implement security controls for cloud and server infrastructure.",
        "required_skills": "AWS, IAM, Linux, Networking, Security Auditing",
        "salary_range": "7-12 LPA"
    },
    {
        "title": "Linux System Administrator",
        "department": "IT Infrastructure",
        "location": "Pune, India",
        "employment_type": "Full Time",
        "experience": "1-3 Years",
        "description": "Maintain Linux servers and troubleshoot system issues.",
        "required_skills": "Linux, Bash, Shell Scripting, Networking, AWS",
        "salary_range": "3-7 LPA"
    },
    {
        "title": "Linux Cloud Support Trainee",
        "department": "Technical Operations",
        "location": "Mysuru, India",
        "employment_type": "Full Time",
        "experience": "Fresher",
        "description": "Support Linux-based cloud environments and daily operations.",
        "required_skills": "Linux, AWS, Networking, Git, Shell Scripting",
        "salary_range": "2.5-4 LPA"
    },
    {
        "title": "Cloud Database Engineer",
        "department": "Database Engineering",
        "location": "Bengaluru, India",
        "employment_type": "Full Time",
        "experience": "2-4 Years",
        "description": "Design and manage cloud database infrastructure.",
        "required_skills": "AWS RDS, DynamoDB, PostgreSQL, MySQL, SQL",
        "salary_range": "6-10 LPA"
    },
    {
        "title": "Cloud Application Deployment Engineer",
        "department": "Application Engineering",
        "location": "Hyderabad, India",
        "employment_type": "Full Time",
        "experience": "1-3 Years",
        "description": "Deploy and maintain applications in cloud environments.",
        "required_skills": "AWS, Docker, Jenkins, Git, Linux",
        "salary_range": "4-8 LPA"
    },
    {
        "title": "Cloud FinOps Analyst",
        "department": "Cloud Financial Operations",
        "location": "Pune, India",
        "employment_type": "Full Time",
        "experience": "1-3 Years",
        "description": "Analyze cloud spending and recommend infrastructure cost optimization.",
        "required_skills": "AWS, Azure, Cloud Cost Management, Excel, Analytics",
        "salary_range": "4-8 LPA"
    },
    {
        "title": "Cloud Disaster Recovery Engineer",
        "department": "Business Continuity",
        "location": "Chennai, India",
        "employment_type": "Full Time",
        "experience": "2-4 Years",
        "description": "Design backup and disaster recovery strategies for cloud systems.",
        "required_skills": "AWS, S3, RDS, Backup, Disaster Recovery, Linux",
        "salary_range": "6-10 LPA"
    },
    {
        "title": "Cloud Automation Developer",
        "department": "Automation Engineering",
        "location": "Bengaluru, India",
        "employment_type": "Full Time",
        "experience": "1-3 Years",
        "description": "Develop automation tools for cloud resource management.",
        "required_skills": "Python, AWS, Terraform, REST API, Git",
        "salary_range": "5-9 LPA"
    },
    {
        "title": "DevOps Graduate Trainee",
        "department": "Graduate Engineering",
        "location": "Pune, India",
        "employment_type": "Full Time",
        "experience": "Fresher",
        "description": "Work with experienced engineers on cloud and DevOps projects.",
        "required_skills": "Linux, Python, Git, AWS, Docker",
        "salary_range": "3-4.5 LPA"
    },
    {
        "title": "Cloud Support Engineer",
        "department": "Cloud Operations",
        "location": "Pune, India",
        "employment_type": "Full Time",
        "experience": "0-2 Years",
        "description": "Provide cloud infrastructure support, monitoring and troubleshooting.",
        "required_skills": "AWS, Linux, Networking, EC2, S3, IAM",
        "salary_range": "3-5 LPA"
    }
]


def seed_jobs():

    db = SessionLocal()

    try:
        added = 0

        for job_data in jobs_data:

            existing = db.query(Job).filter(
                Job.title == job_data["title"],
                Job.location == job_data["location"]
            ).first()

            if existing:
                continue

            job = Job(**job_data, status="Open")

            db.add(job)
            added += 1

        db.commit()

        print(f"Successfully added {added} new DevOps jobs!")

    except Exception as error:

        db.rollback()
        print("Job insertion failed:", error)

    finally:
        db.close()


if __name__ == "__main__":
    seed_jobs()