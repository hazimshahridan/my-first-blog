from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('about',views.webpage2, name='webpage2'),
    path('contact',views.webpage3, name='webpage3'),

]