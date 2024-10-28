import hashlib
import base64
import re
from typing import Optional
from ..repositories.repositories import URLRepository

class URLService:
    BASE62_CHARS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    SIGNATURE_LENGTH = 4
    
    @staticmethod
    def generate_short_code(url: str) -> str:
        url_hash = hashlib.md5(url.encode()).hexdigest()
        
        base = int(url_hash[:8], 16)
        
        base62 = ''
        while base:
            base, rem = divmod(base, 62)
            base62 = URLService.BASE62_CHARS[rem] + base62
        
        signature = hashlib.sha256(url.encode()).hexdigest()[:URLService.SIGNATURE_LENGTH]
        
        return f"{base62}{signature}"

    def create_short_url(self, original_url: str, request) -> dict:
        short_code = self.generate_short_code(original_url)
        url_obj = URLRepository.create_url(original_url, short_code)
        
        short_url = f"{request.scheme}://{request.get_host()}/{url_obj.short_code}"
        return {
            'short_url': short_url,
            'original_url': url_obj.original_url
        }

    def is_valid_short_code(self, short_code: str) -> bool:
        if not short_code:
            return False
            
        if len(short_code) <= self.SIGNATURE_LENGTH:
            return False
            
        base62_part = short_code[:-self.SIGNATURE_LENGTH]
        signature = short_code[-self.SIGNATURE_LENGTH:]
        
        
        if not all(c in self.BASE62_CHARS for c in base62_part):
            return False
            
        try:
            int(signature, 16)
            return len(signature) == self.SIGNATURE_LENGTH
        except ValueError:
            return False

    def get_original_url(self, short_code: str) -> Optional[str]:
    
        if not self.is_valid_short_code(short_code):
            return None
            
        url_obj = URLRepository.get_by_short_code(short_code)
        return url_obj.original_url if url_obj else None