from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('about',views.webpage2, name='webpage2'),
    path('contact',views.webpage3, name='webpage3'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]