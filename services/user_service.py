from models.user_model import User
from repositories.user_repository import UserRepository

class UserService:

    @staticmethod
    def create_user(username, password):
        if not username or not password:
            raise ValueError("Os dados principais do usuário não podem estar vazio.")
        UserRepository.create_user(username, password)

    @staticmethod
    def check_user(username, password):
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            return user.id, user.is_admin
        return None  # Retorna None se a autenticação falhar

    @staticmethod
    def list_users():
        return UserRepository.list_users()