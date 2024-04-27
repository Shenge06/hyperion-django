from django.urls import path
from . import views

app_name = 'user_auth'
urlpatterns = [
    path('', views.user_login, name='login'),
    path('show_user/', views.show_user, name='show_user'),  # Add this URL for showing user info
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
]