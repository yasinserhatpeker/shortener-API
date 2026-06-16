from typing import Optional
from shortener.models import UrlItem
from django.db.models import QuerySet,Q
from django.utils import timezone


def get_active_urls_by_user(*,user) -> QuerySet[UrlItem]:
    return UrlItem.objects.filter(user=user)  # fetch the all urls related to the user


def get_active_url_by_code(*,short_code:str) -> Optional[UrlItem]: # fetch the active short url related to the user
    now = timezone.now()
    try:
     return UrlItem.objects.filter(short_url=short_code).filter(Q(expires_at__isnull=True) | Q(expires_at__gt=now)).get()

    except UrlItem.DoesNotExist:
        return None
    
    
def get_url_code_by_user(*,short_code:str,user) -> Optional[UrlItem]: # fetch the short urls by user
    try:
        return UrlItem.objects.filter(user=user,short_url=short_code)
    except UrlItem.DoesNotExist:
        return None
    