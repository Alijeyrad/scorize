from django.urls import path
from .views import universities, university

app_name = 'home'

urlpatterns = [
    path('', universities, name='universities'),
    path('<int:id>', university, name='university'),
    path('search', universities, name='search'),
]