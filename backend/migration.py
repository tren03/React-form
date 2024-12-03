import sqlite3

conn = None
try:
    conn = sqlite3.connect("./database/tododb.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            taskId INTEGER PRIMARY KEY AUTOINCREMENT,   
            taskTitle TEXT,
            taskDescription TEXT,
            taskCategory TEXT
        )
        """
    )

    tasks = [
        {
            "taskTitle": "Task1",
            "taskDescription": "sample task 1",
            "taskCategory": "High Priority",
        },
        {
            "taskTitle": "Task2",
            "taskDescription": "sample task 2",
            "taskCategory": "Medium Priority",
        },
        {
            "taskTitle": "Task3",
            "taskDescription": "sample task 3",
            "taskCategory": "Low Priority",
        },
    ]

    for task in tasks:
        cursor.execute(
            """
     INSERT INTO tasks (taskTitle, taskDescription, taskCategory)
     VALUES (?, ?, ?)
     """,
            (task["taskTitle"], task["taskDescription"], task["taskCategory"]),
        )

    conn.commit()
    print("Table 'tasks' created successfully and sample data inserted")

except sqlite3.Error as e:
    print(f"An error occurred: {e}")

finally:
    # Ensure the connection is closed
    if conn:
        conn.close()
