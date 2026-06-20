from celery import shared_task
import logging
from django.core.cache import cache
from django.db.models import F
from shortener.models import UrlItem

logger = logging.getLogger(__name__)

@shared_task
def sync_click_counts():
    