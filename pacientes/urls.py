from django.urls import path
from . import views

urlpatterns = [
    path('pacientes/', views.lista_pacientes, name='lista_pacientes'),
    path('pacientes/cadastrar/', views.cadastrar_paciente, name='cadastrar_paciente'),
    path('pacientes/editar/<str:id>/', views.editar_paciente, name='editar_paciente'),
    path('pacientes/remover/<str:id>/', views.remover_paciente, name='remover_paciente'),
    path('pacientes/<str:id>/', views.detalhe_paciente, name='detalhe_paciente'),
]