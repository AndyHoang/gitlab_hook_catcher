# Project Name

Brief project description goes here.

## How to Use Pre-Commit with Gitleaks

Pre-commit is a tool that allows you to define and run Git pre-commit hooks for your project. Gitleaks is a pre-commit hook that scans your project's Git repository for secrets and credentials. Here's how to use Pre-commit with Gitleaks:

1. [Install Pre-commit](https://pre-commit.com/#installation) on your machine.
2. [Install Gitleaks](https://github.com/gitleaks/gitleaks#getting-started)
3. In your project directory, run `pre-commit install` to install the pre-commit hooks for your project.
4. Stage some changes and run `git commit` to trigger the pre-commit hook. If Gitleaks detects any secrets or credentials, the commit will be aborted.

## How to start

PDM is a modern Python package management tool that is used to manage the dependencies of your project. Here's how to install and run basic commands with PDM:

1. [Install PDM](https://pdm.fming.dev/installation/) on your machine.
2. Use `pdm install` to install the packages and their dependencies.
3. Use `pdm run <command>` to run any command inside the virtual environment.

## How to Start server with the App.py in development mode

`app.py` is the main file that contains the FastAPI application logic:

1. Navigate to your project directory and install the necessary packages with `pdm install`.
2. Run `pdm run app.py` to start the server.

## How to Run Tests with Pytest

Pytest is a popular testing framework for Python projects. Here's how to run tests with Pytest:

3. Run `pdm run pytest` to run all tests in the `tests` directory.

