class URLShortenerError(Exception):
    """Base exception class for URL shortener service"""
    pass

class InvalidShortCodeError(URLShortenerError):
    """Raised when the provided short code is invalid"""
    pass
