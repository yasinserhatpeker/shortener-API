from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class UserResponseSerializer(serializers.ModelSerializer): # API -> Client
    class Meta:
        model = User
        fields = ['id','email','username']
        
        

class UserRegisterSerializer(serializers.ModelSerializer): # Client -> API(for validation)
    password = serializers.CharField(write_only=True, validators=[validate_password])
    
    class Meta:
        model=User
        fields=['username','email','password']
        
        