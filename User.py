from werkzeug.security import check_password_hash


class User:
    def __init__(self, username, email, password):
        self.username = username
        self.password = password
        self.email = email

    # нет активации, поэтому всегда true.
    # прикольно, можно имспользоватб, когда нет зависимости от self
    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    # в чате не будет анонимов
    @staticmethod
    def is_anonymous():
        return False

    def get_id(self):
        return self.username

    def check_password(self, password_input):
        return check_password_hash(self.password, password_input)