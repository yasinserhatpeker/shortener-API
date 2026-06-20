from rest_framework.permissions import AllowAny
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from shortener.selectors.selectors import get_active_url_by_code
from django.shortcuts import redirect


class RedirectAPIView(APIView):
    permission_classes=[AllowAny]
    authentication_classes=[]
    
    def get(self,request,short_code):
        
        url_item = get_active_url_by_code(short_code=short_code)
        
        if url_item:
            
            cache.incr(f"clicks_{short_code}")
            return redirect(url_item.original_url)
        
        else:
            return Response({"error":"Url is not found or expired."}, status=status.HTTP_404_NOT_FOUND)
        
        
        
    
       