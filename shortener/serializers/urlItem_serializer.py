from rest_framework import serializers
from shortener.models import UrlItem


class UrlItemResponseSerializer(serializers.ModelSerializer): # API -> Client
    class Meta:
        model=UrlItem
        fields = ['id','short_url','original_url','created_at','expires_at','click_count']
        read_only_fields = ['id','short_url','click_count','created_at']
        

class UrlItemCreateSerializer(serializers.Serializer):   # Client->API (for validation)
    original_url = serializers.URLField(max_length=2048)
    custom_alias = serializers.CharField(max_length=50,required=False, allow_blank=True)