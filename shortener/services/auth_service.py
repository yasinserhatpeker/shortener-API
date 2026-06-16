from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError as DjangoValidationError
from django.contrib.auth.base_user import AbstractBaseUser
from rest_framework.exceptions import ValidationError as DRFValidationError

User = get_user_model()

def create_user(*, email: str, username: str, password: str) -> AbstractBaseUser:
    
    user = User(email=email, username=username)
    user.set_password(password)
    
    try:
        user.full_clean()
    except DjangoValidationError as e:
        raise DRFValidationError(e.message_dict)
        
    user.save()
    return user