# To-Do List CLI

A command-line based task manager built in python that allows users to manage daily tasks efficiently.

## Features

- Add new tasks with priority(High,medium,Low) and due date
- View all tasks with status and priority
- Mark tasks as completed
- View only completed or pending tasks
- Sort tasks by due date and priority
- Edit existing tasks
- Search tasks by keyword
- Remove individual tasks
- Remove all completed tasks
- Persistent storage using JSON

## Technologies used

- Python
- JSON(for data storage)
- File Handling

## How it works

- Tasks are stored as list of dictionaries
- Each task contains:
   - Task name
   - Completion status
   - Priority level
   - Due Date
- Data is saved in `tasks.json` file and loaded when the program starts

## How to run

- Run the script: python todo.py
- Use the menu to interact with the program

## Future improvements

- Improve UI/formatting
- Convert into a GUI or web app

