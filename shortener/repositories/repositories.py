from ..models import URL
from django.db import transaction

class URLRepository:
    @staticmethod
    def create_url(original_url: str, short_code: str) -> URL:
        with transaction.atomic():
            url_obj, created = URL.objects.get_or_create(
                original_url=original_url,
                defaults={'short_code': short_code}
            )
            return url_obj

    @staticmethod
    def get_by_short_code(short_code: str) -> URL:
        try:
            url_obj = URL.objects.get(short_code=short_code)
            url_obj.visits += 1
            url_obj.save()
            return url_obj
        except URL.DoesNotExist:
            return None