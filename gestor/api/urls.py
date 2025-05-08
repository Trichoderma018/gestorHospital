from django.urls import path
from .views import PacientesList, PacientesDetail, DoctoresList, DoctoresDetail, EspecialidadesList, EspecialidadesDetail, CitasList, CitasDetail

urlpatterns = [
    path('pacientes/', PacientesList.as_view(), name='pacientes-list'),
    path('pacientes/<int:pk>/', PacientesDetail.as_view(), name='pacientes-detail'),
    path('doctores/', DoctoresList.as_view(), name='doctores-list'),
    path('doctores/<int:pk>/', DoctoresDetail.as_view(), name='doctores-detail'),
    path('especialidades/', EspecialidadesList.as_view(), name='especialidades-list'),
    path('especialidades/<int:pk>/', EspecialidadesDetail.as_view(), name='especialidades-detail'),
    path('citas/', CitasList.as_view(), name='citas-list'),
    path('citas/<int:pk>/', CitasDetail.as_view(), name='citas-detail'),
]