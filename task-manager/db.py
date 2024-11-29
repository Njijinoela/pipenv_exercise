import sqlite3

def init_db():
    """Initialize the database and create the tasks table if it doesn't exist."""
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    
    # Create tasks table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        status TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
