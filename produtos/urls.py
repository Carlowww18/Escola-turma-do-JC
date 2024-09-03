from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register_aluno, name='register'),
    path('register/create_aluno/', views.register_create , name="create"),
    path('register_admin/', views.register_admin , name="register_admin"),
]