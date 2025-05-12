from django.urls import path
from .views import PacientesListCreateView, PacientesDetailView, DoctoresListCreateView, DoctoresDetailView, CitasListCreateView, CitasDetailView, EspecialidadesListCreateView, EspecialidadesDetailView, DoctoresEspecialidadesListCreateView, DoctoresEspecialidadesDetailView, UserListCreateView, UserDetailView

urlpatterns = [
    path('pacientes/', PacientesListCreateView.as_view(), name='pacientes-list-create'),
    path('pacientes/<int:pk>/', PacientesDetailView.as_view(), name='pacientes-detail'),
    path('doctores/', DoctoresListCreateView.as_view(), name='doctores-list-create'),
    path('doctores/<int:pk>/', DoctoresDetailView.as_view(), name='doctores-detail'),
    path('citas/', CitasListCreateView.as_view(), name='citas-list-create'),
    path('citas/<int:pk>/', CitasDetailView.as_view(), name='citas-detail'),
    path('especialidades/', EspecialidadesListCreateView.as_view(), name='especialidades-list-create'),
    path('especialidades/<int:pk>/', EspecialidadesDetailView.as_view(), name='especialidades-detail'),
    path('doctores-especialidades/', DoctoresEspecialidadesListCreateView.as_view(), name='doctores-especialidades-list-create'),
    path('doctores-especialidades/<int:pk>/', DoctoresEspecialidadesDetailView.as_view(), name='doctores-especialidades-detail'),
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]