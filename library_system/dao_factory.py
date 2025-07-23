from dao.book_dao import BookDAO
from dao.user_dao import UserDAO
from dao.borrowing_dao import BorrowingDAO

class DAOFactory:
    @staticmethod
    def get_dao(dao_type):
        if dao_type == "BookDAO":
            return BookDAO()
        elif dao_type == "UserDAO":
            return UserDAO()
        elif dao_type == "BorrowingDAO":
            return BorrowingDAO()
        else:
            raise ValueError("Unknown DAO type")
