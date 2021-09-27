from django.contrib import admin
from django.urls import path
from .views import PostsViewSet, LoginAuthToken
from . import views

urlpatterns = [
    path('posts/', PostsViewSet.as_view({'get': 'list'})),

    path('login/', LoginAuthToken.as_view()),
    path('registration/', views.register_user)
]