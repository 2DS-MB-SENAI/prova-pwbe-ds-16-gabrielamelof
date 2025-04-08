from django.urls import path
from . import views

urlpatterns = [
    path('api/servicos/', views.servicos),
    path('api/agendamentos/', views.agendamentos),
    path('api/servicos/<int:pk>/', views.pegar_servico),
    path('api/agendamentos/<int:pk>/', views.pegar_agendamento),
]