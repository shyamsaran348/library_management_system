# db_connection.py
import mysql.connector
from mysql.connector import Error
from config import db_config

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance._init_connection()
        return cls._instance

    def _init_connection(self):
        try:
            self.conn = mysql.connector.connect(**db_config)
            if self.conn.is_connected():
                print("Successfully connected to the MySQL database")
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            self.conn = None

    def get_connection(self):
        if not self.conn or not self.conn.is_connected():
            self._init_connection()  # Reinitialize if the connection was closed
        return self.conn

    def close_connection(self):
        if self.conn and self.conn.is_connected():
            self.conn.close()
            print("MySQL connection closed.")
            DatabaseConnection._instance = None

    # Add context management methods
    def __enter__(self):
        return self.get_connection()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_connection()
