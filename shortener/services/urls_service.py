from shortener.models import UrlItem
from django.db import transaction
from rest_framework.exceptions import ValidationError
from shortener.utils.sqids_helper import encode_id


def create_short_url(*,user,original_url:str,custom_alias:str =None) -> UrlItem:
    with transaction.atomic():
        if custom_alias:
            if UrlItem.objects.filter(short_url=custom_alias).exists():
                raise ValidationError({"This custom alias is already using."})
            
            return UrlItem.objects.create(
                original_url=original_url,
                user=user,
                short_url = custom_alias
             )
            
        url_item = UrlItem.objects.create(
            original_url=original_url,
            user = user
        )
        url_item.short_url=encode_id(url_item.id)
        url_item.save(update_fields=['short_url'])
        
        return url_item
        

def delete_short_url(*,url_item:UrlItem)->None:
    url_item.delete()
    