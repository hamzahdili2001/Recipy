# Recipy Website README
This README provides an overview and instructions for setting up and running a recipe website developed using Django for the backend, Vue.js with Vuetify for the frontend, and MySQL for the database. The website includes a Recipe API to manage recipes.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- User registration and authentication system.
- Browse, search, and filter recipes based on various criteria (e.g., category, ingredients).
- Create, read, update, and delete recipes.
- Rate and review recipes.
- User profile management.
- API endpoints for recipe data manipulation.

## Requirements

- Python
- Django
- django-rest-framework
- Vue.js
- Vuetify
- MySQL
more in the requirements.txt

## Installation

1. Clone the repository:

   ```bash
   git clone [https://github.com/your-username/recipe-website.git](https://github.com/hamzahdili2001/Recipy.git)
   ```

2. Navigate to the project directory:

   ```bash
   cd Recipy
   ```

3. Backend setup:

   ```bash
   cd backend
   ```

   - Install Python dependencies:

     ```bash
     pip install -r requirements.txt
     ```

   - Migrate the database:

     ```bash
     python manage.py migrate
     ```

4. Frontend setup:

   ```bash
   cd ../frontend
   ```

   - Install Node.js dependencies:

     ```bash
     npm install
     ```

5. Database setup:

   - Create a MySQL database for the project.
   - Update the database configuration in `backend/settings.py`.

6. Start the backend server:

   ```bash
   python manage.py runserver
   ```

7. Start the frontend server:

   ```bash
   npm run dev
   ```

8. Access the website:

   Open your web browser and go to `http://localhost:3000`.

## Configuration

- Backend:

  - Modify `backend/settings.py` to configure database settings, secret key, allowed hosts, etc.

- Frontend:

  - Modify `frontend/src/config.js` to configure API endpoints, base URL, etc.

## Usage

- Register a new account or login with existing credentials.
- Browse through recipes, search for specific recipes, or filter them by categories, ingredients, etc.
- View recipe details, including ingredients, instructions, ratings, and reviews.
- Create new recipes, edit or delete existing ones.
- like and comment recipes.
- Manage user profile settings.
