from shortener.serializers.urlItem_serializer import UrlItemResponseSerializer,UrlItemCreateSerializer
from shortener.services.urls_service import create_short_url,delete_short_url
from shortener.selectors.selectors import get_active_urls_by_user,get_url_code_by_user
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema,OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import Http404


class UrlCreateAPIView(APIView):   # creating short url from original url
    permission_classes=[IsAuthenticated]
    @extend_schema(
        request=UrlItemCreateSerializer,
        responses={201:UrlItemResponseSerializer},
        summary="Creating Url",
        description="Fetching original url and converts it a short code (short url)"
    )
    
    
    def post(self,request):
        serializer = UrlItemCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        
        url_item = create_short_url(
            user=request.user,
            original_url=serializer.validated_data.get('original_url'),
            custom_alias=serializer.validated_data.get('custom_alias')
        )
        
        return Response(UrlItemResponseSerializer(url_item).data,status=status.HTTP_201_CREATED)
    
    

class UrlListAPIView(APIView):  # get the list of the short url with authentication
    permission_classes=[IsAuthenticated]
    
    @extend_schema(
        request=None,
        responses={200:UrlItemResponseSerializer(many=True)},
        summary="Listing short urls"
    )
    
    def get(self,request):
        user_urls = get_active_urls_by_user(user=request.user)
        serializer = UrlItemResponseSerializer(user_urls,many=True)
        
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    
    
class UrlDetailAPIView(APIView):    # with helper method(get_object) we're deleting the short url effortlessly
    permission_classes=[IsAuthenticated]
    
    def get_object(self,user,short_code):
        url_item = get_url_code_by_user(user=user,short_code=short_code)
        
        if not url_item:
            raise Http404('Cannot found the short url related to the user')
        return url_item
    
    @extend_schema(
        request=None,
        responses={204: None},
        parameters=[
            OpenApiParameter(name='short_code', description='Short code of the URL to delete', required=True, type=OpenApiTypes.STR, location=OpenApiParameter.PATH)
        ],
        summary="Deleting short url",
        description="Deletes the specified short URL related to the authenticated user."
    )
    
    
    def delete(self,request,short_code):
       url_item = self.get_object(request.user,short_code=short_code)
       delete_short_url(url_item=url_item)
       
       return Response(status=status.HTTP_204_NO_CONTENT)
       