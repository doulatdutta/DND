import sqlite3

class MemoryManager:
    def __init__(self):
        self.db_path = "common_memory.sql"
        self.init_db()

    def init_db(self):
        """
        Initialize the memory database to store known tasks and solutions.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL,
                solution TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def get_known_tasks(self):
        """
        Retrieve all known tasks from memory.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT task FROM tasks")
        tasks = [row[0] for row in cursor.fetchall()]
        conn.close()
        return tasks

    def execute_memory_task(self, task):
        """
        Retrieve and execute a task's solution from memory.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT solution FROM tasks WHERE task=?", (task,))
        solution = cursor.fetchone()
        conn.close()
        
        if solution:
            print(f"Executing memory task: {task}")
            exec(solution[0])  # Simplified solution execution
            return f"Executed from memory: {task}"
        else:
            raise Exception(f"No memory found for task: {task}")

    def save_task_solution(self, task, solution):
        """
        Save the task and its solution into memory.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (task, solution) VALUES (?, ?)", (task, solution))
        conn.commit()
        conn.close()
        print(f"Task saved to memory: {task}")

