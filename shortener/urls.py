from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView
from shortener.views.auth_views import RegisterView
from shortener.views.urls_views import UrlCreateView,UrlListView,UrlDetailView
from shortener.views.redirect_views import RedirectView

app_name='shortener'

urlpatterns = [
   
   # auth paths
    path("auth/register/", RegisterView.as_view(), name='register'),
    path("auth/login/", TokenObtainPairView.as_view(), name='login'),
    path("auth/refresh/", TokenRefreshView.as_view(), name='refresh'),
    
    # crud paths
    path("urls/create/", UrlCreateView.as_view(), name='url-create'),
    path("urls/list/",UrlListView.as_view(), name='url-list'),
    path("urls/delete/<str:short_code>/", UrlDetailView.as_view(), name='url-delete'),
    
    #redirect path
    path("<str:short_code>/", RedirectView.as_view(), name="url-redirect"),
]