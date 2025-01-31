# DATAFUN-03-ANALYTICS PROJECT
#### This project demonstrates how to 'get' and 'process' CSV, Excel, Text, and JSON files using Python. The repository contains Python scripts designed to perform data analysis and processing tasks on various datasets.

## Steps for Project Initialization
### 1. Create a New Repository From Scratch
Start by creating a new repository on GitHub. You can follow GitHub's instructions for creating a repository.

### 2. Clone the Repository to Your Local Machine
Clone your new repository using the following command:
git clone https://github.com/youraccount/yourrepo
Hint: Replace youraccount and yourrepo with your actual GitHub username and repository name.

### 3. Add Essential Files
Add necessary files such as .gitignore and requirements.txt to your local repository.

### 4. Add, Commit, and Push Files to GitHub
After adding your files, use the following commands to push them to your GitHub repository:
git add .
git commit -m "Add .gitignore and requirements.txt files"
git push -u origin main
Hint: Replace the commit message with a clear description of what you added or changed. Wrap the commit message in double quotes.

For subsequent changes, you can simply use:
git push

### 5. Set Up Your Python Virtual Environment
Create a local Python virtual environment for your project using the following command:
py -m venv .venv


## Continue With the Repeatable Project Workflow
### 1. Pull the Latest Changes from GitHub
To ensure you're working with the latest version of the project, pull updates from the repository:
git pull origin main

### 2. Activate the Project Virtual Environment
Activate your virtual environment using the command:
.venv\Scripts\activate

### 3. Install Dependencies
Once the virtual environment is activated, install the necessary dependencies listed in requirements.txt:
py -m pip install --upgrade pip setuptools wheel
py -m pip install -r requirements.txt

### 4. Run Scripts
Create a small test script and run it to verify that everything is set up correctly.

### 5. Modify Code and Test Functionality
Make changes to the code as needed, testing the functionality as you go.

### 6. Save Your Work to GitHub
After making changes, save your work and push it to GitHub using:
git add .
git commit -m "Description of changes"
git push -u origin main



## Summary of Common Commands
# Clone the repository
git clone https://github.com/youraccount/yourrepo

# Add and commit files
git add .
git commit -m "Description of changes"
git push -u origin main

# Create a virtual environment
py -m venv .venv

# Activate the virtual environment
.venv\Scripts\activate

# Install dependencies
py -m pip install -r requirements.txt

# Pull the latest changes from GitHub
git pull origin main
