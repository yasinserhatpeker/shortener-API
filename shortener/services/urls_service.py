from shortener.models import UrlItem
from django.core.cache import cache
from django.db import transaction
from rest_framework.exceptions import ValidationError
from shortener.utils.sqids_helper import encode_id


CACHE_TIMEOUT = 60 * 60 * 24


def create_short_url(*,user,original_url:str,custom_alias:str = None) -> UrlItem:
    
    with transaction.atomic():
        if custom_alias:
            if UrlItem.objects.filter(short_url=custom_alias).exists():
                raise ValidationError({"custom_alias":'This custom alias already in use.'})
            
            return UrlItem.objects.create(
                original_url=original_url,
                user=user,
                short_url = custom_alias
             )
            
        url_item = UrlItem.objects.create(
            original_url=original_url,
            user = user
        )
        url_item.short_url=encode_id(db_id=url_item.id)
        
        url_item.save(update_fields=['short_url'])
        
        cache_key = f"url_obj{url_item.short_url}"  ## Write-through Caching
        cache.set(cache_key, url_item, timeout=CACHE_TIMEOUT)
        
        
        return url_item
        

def delete_short_url(*,url_item:UrlItem) -> None:
    
    short_code = url_item.short_url
    cache_key = f"url_obj{short_code}"
    
    url_item.delete()
    
    cache.delete(cache_key)
    