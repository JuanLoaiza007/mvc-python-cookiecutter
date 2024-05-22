# mcv-python-cookiecutter

<p align="center">
⚠️ This template is under development, everything is subject to change. ⚠️
</p>

## Description

This repository contains a Cookiecutter template for initializing Python projects with a focus on the Model-View-Controller (MVC) design pattern. The template supports project initialization and includes configurations for common project needs.
Features

- Supports project setup in **English and Spanish**.
- Pre-configured structure for MVC pattern.
- Includes necessary directories for assets, configurations, models, views and controllers.
- Ready-to-use example files for quick project start.

## Requirements

- `Python 3.8` or higher.
- Cookiecutter installed (pip install cookiecutter).

## Usage

To use this template, follow these steps:

1. Install Cookiecutter if you haven't already:

```
pip install cookiecutter
```

2. Generate a new project using this template:

```
cookiecutter https://github.com/JuanLoaiza007/cookiecutter-python-mvc-template.git
```

Follow the prompts to customize your new project.

## Project Structure

The generated project will have the following structure:

```
project_name/
│
├── assets
│   └── README
│
├── data
│   └── README
│
├── src
│   ├── controllers
│   │   └── __init__.py
│   ├── models
│   │   └── __init__.py
│   └── views
│       └── __init__.py
│
├── test
│   └── __init__.py
│
├── .gitignore
├── LICENSE
├── main.py
├── README.md
└── requirements.txt
```

## Contributing

If you want to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and ensure tests pass.
4. Submit a pull request with a clear description of your changes.
