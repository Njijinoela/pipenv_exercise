import sqlite3

def add_task(description, status="Pending"):
    """Add a new task to the database."""
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    
    # Insert the task into the tasks table
    cursor.execute('''
    INSERT INTO tasks (description, status) VALUES (?, ?)
    ''', (description, status))

    conn.commit()
    conn.close()

def view_tasks():
    """Retrieve and return all tasks from the database."""
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()

    # Select all tasks from the tasks table
    cursor.execute('SELECT id, description, status FROM tasks')
    tasks = cursor.fetchall()

    conn.close()
    return tasks
