
# Library Management System

## Overview
The Library Management System is a web-based application built with Flask and MySQL that helps libraries manage their books, users, and borrowing operations. The system provides an intuitive interface for librarians to add books and users, manage book borrowing and returns, and track the library's inventory.

## Features
- **Book Management**: Add, view, and manage books in the library inventory
- **User Management**: Register and manage library members
- **Borrowing System**: Track book borrowing and returns
- **Fine Calculation**: Automatically calculate fines for late returns
- **Responsive UI**: Clean and user-friendly interface

## Project Structure
```
library_system/
├── app.py                 # Main Flask application
├── config.py              # Database configuration
├── db_connection.py       # Database connection singleton
├── dao_factory.py         # Factory for Data Access Objects
├── dao/                   # Data Access Objects
│   ├── __init__.py
│   ├── book_dao.py        # Book data operations
│   ├── borrowing_dao.py   # Borrowing data operations
│   └── user_dao.py        # User data operations
├── services/              # Business logic services
│   ├── __init__.py
│   ├── book_service.py    # Book-related business logic
│   ├── borrowing_service.py # Borrowing-related business logic
│   └── user_service.py    # User-related business logic
├── static/                # Static assets
│   └── styles.css         # CSS styles
└── templates/             # HTML templates
    ├── add_book.html      # Add book form
    ├── add_user.html      # Add user form
    ├── borrow_book.html   # Borrow book form
    ├── index.html         # Homepage
    ├── return_book.html   # Return book form
    ├── user_list.html     # User listing
    └── view_books.html    # Book listing
```

## Architecture
The application follows a layered architecture pattern:

1. **Presentation Layer**: Flask routes and HTML templates
2. **Service Layer**: Business logic in service classes
3. **Data Access Layer**: DAO classes for database operations
4. **Database Layer**: MySQL database

The system uses the Factory pattern for creating DAO objects and the Singleton pattern for database connections.

## Prerequisites
- Python 3.6+
- MySQL Server
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/library_system.git
   cd library_system
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up the MySQL database:
   - Create a database named `library_system`
   - Import the database schema (SQL file not included in this repository)

5. Configure the database connection:
   - Update the `config.py` file with your MySQL credentials or
   - Set environment variables: `MYSQL_USER`, `MYSQL_PASSWORD`, `MYSQL_HOST`, `MYSQL_DB`

6. Run the application:
   ```
   python app.py
   ```

7. Access the application in your web browser at `http://localhost:5000`

## Database Schema

The system uses the following database tables:

- **Books**: Stores book information (BookID, Title, ISBN, AuthorID, CategoryID, PublicationYear, availability)
- **Users**: Stores user information (UserID, Name, Email, MembershipID)
- **Borrowing**: Tracks borrowing records (BorrowingID, BookID, UserID, BorrowDate, ReturnDate, Status)

## Usage

### Adding a Book
1. Navigate to "Add Book" in the navigation menu
2. Fill in the book details (title, ISBN, author ID, category ID, publication year)
3. Submit the form

### Adding a User
1. Navigate to "Add Member" in the navigation menu
2. Fill in the user details (name, email, membership ID)
3. Submit the form

### Borrowing a Book
1. Navigate to "Borrow Book" in the navigation menu
2. Select the book and user from the dropdown menus
3. Set the borrow and expected return dates
4. Submit the form

### Returning a Book
1. Navigate to "Return Book" in the navigation menu
2. Enter the borrowing ID and user ID
3. Submit the form
4. The system will calculate any applicable fines for late returns

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
- Flask - Web framework
- MySQL Connector - Database connectivity
- Bootstrap - Frontend styling (if used)
