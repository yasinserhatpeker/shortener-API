from shortener.selectors.selectors import get_active_url_by_code
from django.shortcuts import redirect
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.http import Http404
from django.db.models import F


class RedirectAPIView(APIView):
    permission_classes=[AllowAny]
    
    def get(self,request,short_code):
        
        url_item = get_active_url_by_code(short_code=short_code)
        
        if not url_item:
            raise Http404("short url is not found or expires.")
        
        url_item.click_count=F('click_count') + 1
        url_item.save(update_fields=['click_count'])
        
        return redirect(url_item.original_url)