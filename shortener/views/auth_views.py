from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAuthenticated
from drf_spectacular.utils import extend_schema
from shortener.serializers.auth_serializer import UserResponseSerializer,UserRegisterSerializer,UserLogoutSerializer
from shortener.services.auth_service import create_user,logout_user


class RegisterAPIView(APIView):     # Registering new user 
    permission_classes=[AllowAny]
    
    @extend_schema(
        request=UserRegisterSerializer,
        responses={201:UserResponseSerializer},
        summary="Registering a new user",
        description="Registering a new user with JWT tokens",
    )
    
    def post(self,request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = create_user(**serializer.validated_data)
        
        return Response(UserResponseSerializer(user).data, status=status.HTTP_201_CREATED)
        

class LogoutAPIView(APIView):  ## Logging out 
    permission_classes=[IsAuthenticated]
    
    def post(self,request):
        serializer = UserLogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        logout_user(refresh_token=serializer.validated_data['refresh_token'])
        
        return Response(status=status.HTTP_204_NO_CONTENT)