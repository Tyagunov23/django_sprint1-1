from django.urls import path
from .views import about, rules

app_name = 'pages'

urlpatterns = [
    path('about/', about, name='about'),  # Страница "О нас"
    path('rules/', rules, name='rules'),  # Страница "Правила"
]
