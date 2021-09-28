from django.contrib import admin
from django.urls import path
from .views import PostsViewSet, LoginAuthToken, UserPostsView
from . import views

urlpatterns = [
    # auth
    path('login/', LoginAuthToken.as_view()),
    path('registration/', views.register_user),
    # path('reset-password/'),
    # path('forgot-password/'),
    # path('google-auth'),
    # path('logout'),

    # social-media-app
    path('posts/', PostsViewSet.as_view({'get': 'list'})),
    path('user-posts/', UserPostsView.as_view()),
]