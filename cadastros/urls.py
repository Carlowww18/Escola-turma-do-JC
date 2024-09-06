from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),

    #REGISTERS
    path('register/', views.register_aluno, name='register_aluno'),
    path('register/create_aluno/', views.create_aluno , name="create_aluno"),
    path('register_admin/', views.register_admin , name="register_admin"),

    #LISTS
    path('boletim/', views.boletim , name="boletim"),

    #UPDATE
    path('update_aluno/<int:id>', views.update_aluno, name='update_aluno')
]