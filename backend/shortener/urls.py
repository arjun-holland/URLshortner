from django.urls import path
from .views import ShortenURLView, RedirectURLView

urlpatterns = [
    path('api/shorten', ShortenURLView.as_view(), name='shorten_url'),
    path('<str:short_code>/', RedirectURLView.as_view(), name='redirect_url'),
]
