from shortener.serializers.auth_serializer import UserResponseSerializer,UserRegisterSerializer
from shortener.services.auth_service import create_user
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny


class RegisterView(APIView):     # Registering new user 
    permission_classes=[AllowAny]
    
    def post(self,request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = create_user(**serializer.validated_data)
        
        return Response(UserResponseSerializer(user).data, status=status.HTTP_201_CREATED)
        
