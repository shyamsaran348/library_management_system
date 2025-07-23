from db_connection import DatabaseConnection
from mysql.connector import Error
class UserDAO:
    def __init__(self):
        self.conn = DatabaseConnection().get_connection()

    def add_user(self, name, email, membership_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO Users (Name, Email, MembershipID) VALUES (%s, %s, %s)",
                (name, email, membership_id)
            )
            self.conn.commit()
            cursor.close()
        except Error as e:
            # Check for specific error code for duplicate email
            if e.errno == 1062:  # MySQL error code for duplicate entry
                raise ValueError("Email already exists")
            else:
                raise e

    def get_users(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Users")
        users = cursor.fetchall()
        cursor.close()
        return users
