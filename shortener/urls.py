from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView
from shortener.views.auth_views import RegisterAPIView,LogoutAPIView
from shortener.views.urls_views import UrlCreateAPIView,UrlDetailAPIView,UrlListAPIView
from shortener.views.redirect_views import RedirectAPIView

app_name='shortener'

urlpatterns = [
   
   # auth paths
    path("auth/register/", RegisterAPIView.as_view(), name='register'),
    path("auth/login/", TokenObtainPairView.as_view(), name='login'),
    path("auth/refresh/", TokenRefreshView.as_view(), name='refresh'),
    path("auth/logout/", LogoutAPIView.as_view(), name='logout'),
    
    # crud paths
    path("urls/create/", UrlCreateAPIView.as_view(), name='url-create'),
    path("urls/list/",UrlListAPIView.as_view(), name='url-list'),
    path("urls/delete/<str:short_code>/", UrlDetailAPIView.as_view(), name='url-delete'),
    
    #redirect path
    path("<str:short_code>/", RedirectAPIView.as_view(), name="url-redirect"),
]