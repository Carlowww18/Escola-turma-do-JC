from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register_aluno, name='register'),
    path('register/create/', views.register_create , name="create"),
   
]