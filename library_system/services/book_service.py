from dao_factory import DAOFactory
from db_connection import DatabaseConnection

class BookService:
    def __init__(self):
        self.book_dao = DAOFactory.get_dao("BookDAO")

    def add_book(self, title, isbn, author_id, category_id, publication_year):
        self.book_dao.add_book(title, isbn, author_id, category_id, publication_year)

    def list_books(self):
        # Fetch only available books
        query = "SELECT * FROM books WHERE availability = TRUE"
        with DatabaseConnection() as db:
            cursor = db.cursor(dictionary=True)
            cursor.execute(query)
            available_books = cursor.fetchall()
            cursor.close()
        return available_books

    def get_book_by_id(self, book_id):
        # Fetch a specific book by ID
        query = "SELECT * FROM books WHERE BookID = %s"
        with DatabaseConnection() as db:
            cursor = db.cursor(dictionary=True)
            cursor.execute(query, (book_id,))
            book = cursor.fetchone()
            cursor.close()
        return book

    def update_availability(self, book_id, available):
        # Update the availability of a specific book
        query = "UPDATE books SET availability = %s WHERE BookID = %s"
        with DatabaseConnection() as db:
            cursor = db.cursor()
            cursor.execute(query, (available, book_id))
            db.commit()
            cursor.close()
