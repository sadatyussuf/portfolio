# Setting Up and Cloning a Django Project from GitHub

This guide will walk you through the process of setting up your local environment and cloning a Django project from GitHub. Follow these steps to get started with the project.

## Prerequisites

Before you begin, make sure you have the following installed on your machine:

1. **Python**: Install Python from [python.org](https://www.python.org/downloads/).
2. **pip**: Python package installer. It usually comes with Python. You can check by running `pip --version`.
3. **virtualenv**: Install using `pip install virtualenv`.

## Step 1: Clone the Repository

Open your terminal or command prompt and navigate to the directory where you want to store your project.

```bash
# Replace 'project-name' with the actual name of the project
git clone https://github.com/username/project-name.git
```

This will clone the repository to your local machine.

## Step 2: Create a Virtual Environment

### Navigate into the project directory:

```bash
cd project-name
```

### Create a virtual environment:

```bash
# On Windows
python -m venv venv

# On macOS and Linux
python3 -m venv venv

```

### Activate the virtual environment:

```bash
# On Windows bash shell (check if it works on command prompt or powershell)
source venv\Scripts\activate

# On macOS and Linux
source venv/bin/activate
```

## Step 3: Install Dependencies

With the virtual environment activated, install the project dependencies:

```bash
# Note: the file called also be called requirement.txt, check first
pip install -r requirements.txt
```

This command installs all the necessary packages specified in the requirements.txt file.

## Step 4: Apply Migrations

### Apply the database migrations:

```bash
python manage.py migrate
```

## Step 5: Create a Superuser (Optional)

If the project includes authentication and you want to create an admin user, run:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up the superuser account.This allows you to use django admin page (cool stuff)

## Step 6: Run the Development Server

### Start the Django development server:

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ in your web browser to see the application running.

## Step 7: Create a .env File (Additional Steps Optional)

If you don't find a .env file then you have to create a .env file in the project root and include variables like DEBUG, SECRET_KEY, etc. Make sure to add .env to your .gitignore file.

## That's it! You've successfully set up and cloned a Django project on your local machine. Happy coding!
