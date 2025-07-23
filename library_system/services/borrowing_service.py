from dao_factory import DAOFactory
class BorrowingService:
    def __init__(self):
        self.borrowing_dao = DAOFactory.get_dao("BorrowingDAO")
        self.book_dao = DAOFactory.get_dao("BookDAO")

    def borrow_book(self, book_id, user_id, borrow_date, return_date):
        # Borrowing the book by adding a new record to the borrowing table
        self.borrowing_dao.add_borrowing(book_id, user_id, borrow_date, return_date)
        
        # Update book availability to false since it's now borrowed
        self.book_dao.update_availability(book_id, False)

    def list_borrowing_history(self):
        # Retrieve the borrowing history
        return self.borrowing_dao.get_borrowing_history()

    def return_book(self, borrowing_id, user_id):
        # Use DAO to get the borrowing history
        borrowing_history = self.borrowing_dao.get_borrowing_history()

        # Find the specific borrowing record
        borrowing_record = next((record for record in borrowing_history if record['borrowingid'] == borrowing_id and record['user_id'] == user_id), None)
        
        if not borrowing_record:
            return "Error: Borrowing record not found."

        # Get the return date from the record and calculate fine if necessary
        return_date = datetime.strptime(borrowing_record['ReturnDate'], '%Y-%m-%d')
        current_date = datetime.now()

        # Check if the book is returned late
        if current_date > return_date:
            delay_days = (current_date - return_date).days
            fine = delay_days * 10  # Fine calculation: 10 rupees per day
            message = f"The book is returned late. Fine: {fine} rupees."
        else:
            fine = 0
            message = "Book returned on time. No fine."

        # Mark the borrowing record as returned
        self.borrowing_dao.update_borrowing_as_returned(borrowing_id, user_id)

        # Update the availability of the book in the books table
        book_id = borrowing_record['BookID']
        self.book_dao.update_availability(book_id, True)

        return message
