from db_connection import DatabaseConnection
class BookDAO:
    def __init__(self):
        self.conn = DatabaseConnection().get_connection()

    def add_book(self, title, isbn, author_id, category_id, publication_year):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO Books (Title, ISBN, AuthorID, CategoryID, PublicationYear) VALUES (%s, %s, %s, %s, %s)",
            (title, isbn, author_id, category_id, publication_year)
        )
        self.conn.commit()
        cursor.close()

    def get_books(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Books")
        books = cursor.fetchall()
        cursor.close()
        return books
