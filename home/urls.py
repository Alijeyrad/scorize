from django.urls import path
from .views import universities, university, filter_uni

app_name = 'home'

urlpatterns = [
    path('', universities, name='universities'),
    path('<int:id>', university, name='university'),
    path('<str:keyword>', filter_uni, name='filter'),
]