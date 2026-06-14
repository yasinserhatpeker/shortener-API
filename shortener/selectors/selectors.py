from typing import Optional
from shortener.models import UrlItem
from django.db.models import QuerySet,Q
from django.utils import timezone


def get_active_urls(*,user) -> QuerySet[UrlItem]:
    return UrlItem.objects.filter(user=user)



def get_active_url_by_code(*,short_code:str) -> Optional[UrlItem]:
    now = timezone.now()
    try:
     return UrlItem.objects.filter(short_url=short_code).filter(Q(expires_at__isnull=True) | Q(expires_at__gt=now)).get()

    except UrlItem.DoesNotExist:
        return None