from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('create/', views.news_create, name='create'),
    path('category/<str:category>/', views.news_by_category, name='category'),
    path('detail/<int:news_id>/', views.news_detail, name='detail'),
]
