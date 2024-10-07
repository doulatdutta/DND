import sqlite3
from sqlite3 import Error
from datetime import datetime

class MemoryHandler:
    def __init__(self, db_file='Common_Memory/common_memory.sql'):
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """
        Creates a database connection to the SQLite database.
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"Error '{e}' occurred")
        return conn

    def store_knowledge(self, topic, content):
        """
        Stores knowledge in the database.
        """
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO knowledge (topic, content) VALUES (?, ?)", (topic, content))
        self.connection.commit()
        print(f"Knowledge stored: {topic}")

    def retrieve_knowledge(self, topic):
        """
        Retrieves knowledge based on the topic.
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT content FROM knowledge WHERE topic = ?", (topic,))
        rows = cursor.fetchall()
        if rows:
            return rows[0][0]
        else:
            print("No knowledge found for the specified topic.")
            return None

    def update_memory(self, id, new_memory):
        """
        Updates a memory entry in the database.
        """
        cursor = self.connection.cursor()
        cursor.execute("UPDATE memories SET memory = ?, updated_at = ? WHERE id = ?", 
                       (new_memory, datetime.now(), id))
        self.connection.commit()
        print(f"Memory updated for ID: {id}")

    def close_connection(self):
        """
        Closes the database connection.
        """
        if self.connection:
            self.connection.close()
            print("Connection to SQLite DB closed.")
