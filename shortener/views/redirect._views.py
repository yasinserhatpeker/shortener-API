from shortener.selectors.selectors import get_active_url_by_code
from django.shortcuts import redirect
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.http import Http404
from django.db.models import F


class RedirectView(APIView):
    permission_classes=[AllowAny]
    
    def get(self,request,short_code):
        