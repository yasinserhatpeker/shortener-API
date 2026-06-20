from celery import shared_task
import logging
from django.core.cache import cache
from django.db.models import F
from shortener.models import UrlItem

logger = logging.getLogger(__name__)

@shared_task
def sync_click_counts():
    
    keys = cache.keys('click_*')
    
    if not keys:
        logger.info("There's no count info to synchronize")
        return 'No transcation needed.'

    updated_count = 0
    
    for key in keys:
        short_code = key.split('click_')[-1]
        clicks = cache.get(key)
        
        if clicks and int(clicks) > 0:
            try:
                updated_rows = UrlItem.objects.filter(short_url = short_code).update(
                    click_count =F('click_count') + int(clicks)
                )
                if updated_rows > 0:
                    cache.delete(key)
                    updated_count += 1
                else:
                    logger.warning("")
        
        