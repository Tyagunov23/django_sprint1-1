
from django.urls import path

from .views import index, post_detail, category_post


app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('posts/<int:id>/', post_detail, name='detail'),
    path('category/<slug:category_slug>/', category_post, name='category'),
]
