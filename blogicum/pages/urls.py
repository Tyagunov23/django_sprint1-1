from .views import about, rules

from django.urls import path

app_name = 'pages'

urlpatterns = [
    path('about/', about, name='about'),  # Страница "О нас"
    path('rules/', rules, name='rules'),  # Страница "Правила"
]
