from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):  # custom user model with email
      email = models.EmailField(unique=True)
      
      USERNAME_FIELD='email'
      
      REQUIRED_FIELDS=['username']
      
      def __str__(self):
            return self.email
      