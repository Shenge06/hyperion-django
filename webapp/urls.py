from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup_page, name='signup_page'),
    path('login/', views.login_page, name='login_page'),
    path('polls/', include('polls.urls')), 
    path('blog/', include('blog.urls')), 
]
