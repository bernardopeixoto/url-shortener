from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect

from .exceptions.exceptions import InvalidShortCodeError
from .serializers import URLCreateSerializer, URLResponseSerializer
from .services.services import URLService

class ShortenURLView(APIView):
    def post(self, request):
        serializer = URLCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        url_service = URLService()
        result = url_service.create_short_url(serializer.validated_data['url'], request)
          
        response_serializer = URLResponseSerializer(data=result)
        response_serializer.is_valid()
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

class RedirectURLView(APIView):
    def get(self, request, short_code):
        url_service = URLService()
        
        try:
            original_url = url_service.get_original_url(short_code)
            return redirect(original_url)
            
        except InvalidShortCodeError as e:
            return JsonResponse({
                'error': str(e),
                'status': 'error'
            }, status=400)
            
        except Exception as e:
            return JsonResponse({
                'error': 'An unexpected error occurred',
                'status': 'error'
            }, status=500)