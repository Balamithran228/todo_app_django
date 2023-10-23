# todo_app_django
# To-Do App Readme

## Overview

This To-Do Web Application, built using Django, is designed to help users manage their tasks and stay organized. It offers a user-friendly interface for adding, updating, and marking tasks as complete.

## Features

- Task Management: Create, update, and delete tasks.
- Task Priority: Assign priority levels to tasks.
- Task Completion: Mark tasks as complete.
- User Authentication: Register and log in to manage personal tasks.
- User Profiles: Customize user profiles.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Balamithran228/todo-app.git
   ```

2. Navigate to the project directory:

   ```bash
   cd todo-app
   ```

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

6. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

7. Create a superuser account to manage the admin panel:

   ```bash
   python manage.py createsuperuser
   ```

8. Start the development server:

   ```bash
   python manage.py runserver
   ```

The application should now be accessible at `http://localhost:8000/` in your web browser.

## Usage

1. **Registration and Login**: Start by registering a new user account or log in if you already have one.

2. **Adding Tasks**: Once logged in, you can add new tasks by clicking the "Add Task" button.

3. **Updating and Completing Tasks**: Edit tasks by clicking the pencil icon, and mark them as complete by checking the checkbox.

4. **User Profile**: You can customize your user profile, including your profile picture.

5. **Admin Panel**: Access the admin panel at `http://localhost:8000/admin/` to manage tasks and users.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test thoroughly.
4. Create a pull request.

## License

This To-Do App is open-source and available under the [MIT License](LICENSE.md).
