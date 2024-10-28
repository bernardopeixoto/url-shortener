from django.urls import path
from . import views

urlpatterns = [
    path('shorten', views.ShortenURLView.as_view(), name='shorten-url'),
    path('<str:short_code>', views.RedirectURLView.as_view(), name='redirect-url'),
]