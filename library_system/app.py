import os
from flask import Flask, render_template, request, redirect, url_for, flash
from mysql.connector import Error
from db_connection import DatabaseConnection
from services.book_service import BookService
from services.user_service import UserService
from services.borrowing_service import BorrowingService
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'your-secret-key')  # Set your secret key for session management

# Home route - displays the books and users on the homepage
@app.route('/')
def index():
    book_service = BookService()
    books = book_service.list_books()  # Get list of books from the service
    user_service = UserService()
    users = user_service.list_users()  # Get list of users from the service
    return render_template('index.html', books=books, users=users)

# Route to display the list of users
@app.route('/user_list')
def user_list():
    user_service = UserService()
    users = user_service.list_users()  # Get list of users from the service
    return render_template('user_list.html', users=users)

# Route to display the list of books
@app.route('/view_books')
def view_books():
    book_service = BookService()
    books = book_service.list_books()  # Get list of books from the service
    return render_template('view_books.html', books=books)

# Route to display the form and handle adding a user
@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['userName']
        email = request.form['email']
        membership_id = request.form['membershipID']

        user_service = UserService()
        try:
            user_service.add_user(name, email, membership_id)
            flash("User added successfully!", "success")  # Success message
        except Error as e:
            if "Duplicate entry" in str(e):  # Check for duplicate email error
                flash("Error: Email already exists!", "error")  # Show error message
            else:
                flash(f"Error: {e}", "error")  # General error message
        
        return redirect(url_for('user_list'))  # Redirect to the user list page

    # GET method renders the form to add a user
    return render_template('add_user.html')

# Route to handle adding a book
@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        isbn = request.form['isbn']
        author_id = request.form['author']
        category_id = request.form['category']
        publication_year = request.form['publicationYear']
        
        book_service = BookService()
        book_service.add_book(title, isbn, author_id, category_id, publication_year)
        flash('Book added successfully!', 'success')  # Show success message
        return redirect(url_for('view_books'))  # Redirect to the books list
    
    # GET method renders the form to add a book
    return render_template('add_book.html')

# Route to handle borrowing a book
@app.route('/borrow_book', methods=['GET', 'POST'])
def borrow_book():
    if request.method == 'POST':
        # Get the form data from the POST request
        book_id = request.form['borrowBookID']
        user_id = request.form['borrowUserID']
        borrow_date = request.form['borrowDate']
        return_date = request.form['returnDate']
        
        # Call the borrowing service to handle the borrowing logic
        book_service = BookService()
        book = book_service.get_book_by_id(book_id)
        
        if not book['availability']:
            flash("Error: Book is currently unavailable for borrowing.", "error")
            return redirect(url_for('index'))
        
        borrowing_service = BorrowingService()
        borrowing_service.borrow_book(book_id, user_id, borrow_date, return_date)
        
        # Update book availability to false
        book_service.update_availability(book_id, False)
        flash("Book borrowed successfully!", "success")
        return redirect(url_for('index'))
    
    # If it's a GET request, render the borrow book form
    books = BookService().list_books()  # Fetch the list of books
    users = UserService().list_users()  # Fetch the list of users
    return render_template('borrow_book.html', books=books, users=users)

# Route to handle returning a book
@app.route('/return_book', methods=['GET', 'POST'])
def return_book():
    if request.method == 'POST':
        borrowing_id = request.form['borrowing_id']
        user_id = request.form['user_id']
        
        borrowing_service = BorrowingService()
        message = borrowing_service.return_book(borrowing_id, user_id)
        
        flash(message, "info")
        return redirect(url_for('index'))
    
    # Render the return book form for GET requests
    return render_template('return_book.html')

@app.teardown_appcontext
def close_connection(exception):
    db_connection = DatabaseConnection()
    db_connection.close_connection()  # Close DB connection when app stops

if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode for development
