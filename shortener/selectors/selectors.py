from typing import Optional
from django.core.cache import cache
from shortener.models import UrlItem
from django.db.models import QuerySet,Q
from django.utils import timezone

CACHE_TIMEOUT = 60 * 60 * 24

def get_active_urls_by_user(*,user) -> QuerySet[UrlItem]:
    return UrlItem.objects.filter(user=user)  # fetch the all urls related to the user


def get_active_url_by_code(*,short_code:str) -> Optional[UrlItem]: # fetch the active short url related to the user
    now = timezone.now()
    cache_key = f"url_obj_{short_code}"
    
    cached_item = cache.get(cache_key)
    
    if cached_item:
        if cached_item.expires_at and cached_item.expires_at < now:
            cache.delete(cache_key)
        else:
            return cached_item
    try:
     url_item = UrlItem.objects.filter(short_url=short_code).filter(Q(expires_at__isnull=True) | Q(expires_at__gt=now)).get()
     
     cache.set(cache_key, url_item , timeout =CACHE_TIMEOUT)
     return url_item
 
    except UrlItem.DoesNotExist:
        return None
    
    
def get_url_code_by_user(*,short_code:str,user) -> Optional[UrlItem]: # fetch the short urls by user
    try:
        return UrlItem.objects.get(user=user,short_url=short_code)
    
    except UrlItem.DoesNotExist:
        return None
    