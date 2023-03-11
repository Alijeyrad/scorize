from django.urls import path
from .views import universities

app_name = 'home'

urlpatterns = [
    path('', universities, name='universities'),
]