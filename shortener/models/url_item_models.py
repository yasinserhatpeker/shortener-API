from django.conf import settings
from django.db import models


class UrlItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='urls')
    
    original_url = models.URLField(max_length=2048)
    short_url = models.CharField(max_length=50,blank=True,unique=True,null=True,db_index=True)
    click_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at =models.DateTimeField(blank=True,null=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.original_url} -> {self.short_url}"