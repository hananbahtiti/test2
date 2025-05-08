import bcrypt
from django.core.exceptions import ValidationError
from ..models import CustomUser

class UserService:
    @staticmethod
    def is_email_taken(email: str) -> bool:
        return CustomUser.objects.filter(email=email).exists()

    @staticmethod
    def hash_password(password: str) -> str:
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    
    @classmethod
    def create_user(cls, name: str, email: str, password: str) -> CustomUser:
        print("Creating user...") 
        if cls.is_email_taken(email):
            raise ValidationError("Email already exists")

        hashed_password = cls.hash_password(password)

        user = CustomUser.objects.create(name=name, email=email, password=hashed_password)
        print("User created:", user)
        return user
