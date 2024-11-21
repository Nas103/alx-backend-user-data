# 0x03. User Authentication Service

## Overview

This project focuses on implementing a basic user authentication service to understand the foundational mechanisms of user authentication. The project uses Flask and SQLAlchemy to build and manage the system. While it is recommended to use established frameworks for such tasks in real-world applications, this project is designed for learning purposes.

---

## Learning Objectives

By completing this project, you will learn to:
- Declare API routes in a Flask application.
- Get and set cookies in Flask.
- Retrieve form data from HTTP requests.
- Return appropriate HTTP status codes.
- Use SQLAlchemy to define and manage database models.

---

## Requirements

- All code is executed on **Ubuntu 18.04 LTS** using `python3` (version 3.7).
- Follow the **pycodestyle** guidelines (version 2.5).
- Use **SQLAlchemy 1.3.x** for database interaction.
- Ensure all modules, classes, and functions are fully documented with clear explanations.
- Annotate all functions with type hints.
- Interact with the database only through public methods of `Auth` and `DB`.

---

## Dependencies

Before starting, install the required dependencies:
```bash
pip3 install bcrypt flask sqlalchemy
