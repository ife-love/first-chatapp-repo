from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_page, name='register'),
    path('', views.home_page, name='home'),
    path('room/<str:pk>/', views.room_page, name='room'),
    path('profile/<str:pk>/', views.user_profile, name='user-profile'),
    path('create-room/', views.create_room, name='create-room'),
    path('update-room/<str:pk>/', views.update_room, name='update-room'),
    path('delete-room/<str:pk>/', views.delete_room, name='delete-room'),
    path('delete-message/<str:pk>/', views.delete_message, name='delete-message'),
    path('update-message/<str:pk>/', views.update_message, name='update-message'),
    path('delete-home-message/<str:pk>/', views.delete_home_message, name='delete-home-message'),
]