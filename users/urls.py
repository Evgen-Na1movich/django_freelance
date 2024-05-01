from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),  # http://127.0.0.1:8000/users/login/
    path('register/', views.register, name='register'),  # http://127.0.0.1:8000/users/register/

]
