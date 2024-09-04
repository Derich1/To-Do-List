# To-do List

#### Video Demo: <URL HERE>

#### Description:
This project is a comprehensive task management website developed using JavaScript, Python, Flask, and SQLite. It provides a user-friendly interface for managing tasks, allowing users to create, edit, delete, and organize their tasks effectively. The application is designed to be both functional and visually appealing, ensuring a smooth user experience.

## Features

- **User Authentication**: Allows users to register, log in, and manage their accounts securely.
- **Task Management**: Users can create, view, edit, and delete tasks.
- **Responsive Design**: The website is designed to be responsive and accessible on various devices, including desktops, tablets, and smartphones.
- **Dynamic UI**: Utilizes JavaScript to enhance the user interface with dynamic elements such as task editing and resizing text areas.

## Usage

### Account Registration

- Visit the `register.html` page to create a new account.
- Enter a valid username, email, and password. The system ensures that all required fields are filled out before submission.
- Upon successful registration, you will be redirected to the login page.

### User Login

- Navigate to the `login.html` page.
- Enter your credentials to access your account. The system will validate the username and password.
- Once logged in, you will be directed to the homepage where you can manage your tasks.

### Managing Tasks

- On the `index.html` page, you can view a list of your tasks.
- To create a new task, go to the `task.html` page, fill in the task details, and submit the form. The task will be saved in the database.
- Tasks can be edited or deleted directly from the `index.html` page. Click the edit button to modify task details, and use the delete button to remove a task.

## Backend

- **`app.py`**: The core of the backend logic, handling user authentication, task management, and server-side operations. It includes routes for account creation, login, logout, and task CRUD operations.
- **`helpers.py`**: Contains utility functions such as `login_required`, which enforces user authentication before allowing access to certain functionalities. This modular approach helps keep the code organized and maintainable.

## Frontend

- **`layout.html`**: Serves as the main template file for the website. It defines the overall layout and includes placeholders for dynamic content.
- **`index.html`**: The homepage, which is accessible only to logged-in users. It displays a list of tasks with options to edit or delete each one. The page also includes JavaScript functionality for interactive elements.
- **`login.html`**: The login page for existing users. It includes form validation to ensure that all required fields are completed and provides error messages for invalid inputs.
- **`register.html`**: The registration page where new users can sign up for an account. The form captures user information and validates it before creating a new account.
- **`task.html`**: The page for creating new tasks. Users can enter task details and submit them to be stored in the database.

## JavaScript

- **`task.html`**: Includes JavaScript code to dynamically adjust the size of the textarea used for task descriptions. This ensures that the text area expands as needed to accommodate the user's input without requiring manual resizing.
- **`index.html`**: Manages task editing and deletion. JavaScript functions handle the visibility of edit and delete buttons, display edit forms, and update tasks in real-time. The code also ensures that the save button replaces the edit and delete buttons while editing.

## Database

- **`project.db`**: An SQLite database used to store user information and tasks. It supports various operations such as creating, updating, and deleting records. The database schema is designed to maintain data integrity and facilitate efficient querying.

## Styling

- **`styles.css`**: Defines the visual appearance of the website, including fonts, colors, and animations. The stylesheet is responsible for creating a cohesive and attractive design, enhancing user experience with smooth transitions and responsive elements.
