from dao_factory import DAOFactory

class UserService:
    def __init__(self):
        self.user_dao = DAOFactory.get_dao("UserDAO")

    def add_user(self, name, email, membership_id):
        self.user_dao.add_user(name, email, membership_id)

    def list_users(self):
        return self.user_dao.get_users()
