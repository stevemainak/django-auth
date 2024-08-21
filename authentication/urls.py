from django.urls import path
from authentication import views

urlpatterns=[
    path('register', views.RegisterAPIVIew.as_view(), name='register'),
    path('login', views.LoginAPIVIew.as_view(), name='login'),
]