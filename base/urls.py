from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),

    path('login-page', views.login_page, name='login-page'),
    path('logout-user', views.logout_user, name='logout-user'),
    path('register', views.register_user, name='register'),

    path('room/<str:pk>/', views.room, name='room'),
    path('create-room', views.create_room, name='create-room'),
    path('update-room/<str:pk>/', views.update_room, name='update-room'),
    path('delete-room/<str:pk>/', views.delete, name='delete-room'),
    path('delete-message/<str:pk>/', views.delete_message, name='delete-message')
]
