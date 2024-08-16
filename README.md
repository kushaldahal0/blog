# Django Blog Project

## Overview

This is a Django-based blog application that includes features such as user authentication, blog posting, commenting, and more. The project is styled with Tailwind CSS and uses Font Awesome for icons.

## Features

- User registration and authentication
- Blog creation and management
- Commenting system with replies
- Responsive design using Tailwind CSS
- Dynamic content display

## Prerequisites

- Python 3.8 or higher
- Django 4.2 or higher
- PostgreSQL (or other supported databases)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/kushaldahal0/blog.git
   cd blog
   ```
2. **Create a Virtual Environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment:**
   ```bash
   source venv/bin/activate
   ```
   or in windows
   ```cmd
   venv\Scripts\activate
   ```
4. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Apply Migrations:**
   ```bash
   python manage.py migrate
   ```
6. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```
Acknowledgements<br>
Django: A high-level Python web framework that encourages rapid development.<br>
Tailwind CSS: A utility-first CSS framework for creating custom designs.<br>
Font Awesome: Provides scalable vector icons.
