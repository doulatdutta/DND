import sqlite3

class KnowledgeBase:
    def __init__(self, db_path='Common_Memory/common_memory.db'):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.create_table()

    def create_table(self):
        """
        Creates the knowledge base table if it doesn't already exist.
        """
        query = '''
        CREATE TABLE IF NOT EXISTS knowledge (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            solution TEXT NOT NULL
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def save_task_solution(self, task, solution):
        """
        Saves the task and corresponding solution to the knowledge base.
        """
        query = 'INSERT INTO knowledge (task, solution) VALUES (?, ?)'
        self.conn.execute(query, (task, solution))
        self.conn.commit()
        print(f"Saved solution for task: {task} in knowledge base.")

    def get_solution(self, task):
        """
        Retrieves the solution for a given task from the knowledge base.
        """
        query = 'SELECT solution FROM knowledge WHERE task = ?'
        cursor = self.conn.execute(query, (task,))
        result = cursor.fetchone()
        return result[0] if result else None

    def task_exists(self, task):
        """
        Checks if a task already exists in the knowledge base.
        """
        query = 'SELECT 1 FROM knowledge WHERE task = ?'
        cursor = self.conn.execute(query, (task,))
        return cursor.fetchone() is not None

    def close(self):
        """
        Closes the connection to the knowledge base.
        """
        self.conn.close()
