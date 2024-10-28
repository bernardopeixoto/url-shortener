from rest_framework import serializers
from .models import URL

class URLCreateSerializer(serializers.Serializer):
    url = serializers.URLField(max_length=2048)

class URLResponseSerializer(serializers.Serializer):
    short_url = serializers.CharField()