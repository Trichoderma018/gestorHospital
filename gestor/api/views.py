from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Pacientes, Doctores, Citas, Especialidades, DoctoresEspecialidades
from django.contrib.auth.models import User
from .serializers import PacientesSerializer, DoctoresSerializer, CitasSerializer, EspecialidadesSerializer, DoctoresEspecialidadesSerializer, UserSerializer
from rest_framework.permissions import BasePermission, IsAuthenticated

# Permisos
class IsAdminUserGroup(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='admin').exists()

#Vistas de los modelos creados por Django


# Modelo usuario
class UserListCreateView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


#Visatas de los modelos creados por el desarrollador
class PacientesListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Pacientes.objects.all()
    serializer_class = PacientesSerializer

class PacientesDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUserGroup, IsAuthenticated]
    queryset = Pacientes.objects.all()
    serializer_class = PacientesSerializer

class DoctoresListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Doctores.objects.all()
    serializer_class = DoctoresSerializer

class DoctoresDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUserGroup, IsAuthenticated]
    queryset = Doctores.objects.all()
    serializer_class = DoctoresSerializer

class CitasListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Citas.objects.all()
    serializer_class = CitasSerializer

class CitasDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUserGroup, IsAuthenticated]
    queryset = Citas.objects.all()
    serializer_class = CitasSerializer

class EspecialidadesListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Especialidades.objects.all()
    serializer_class = EspecialidadesSerializer

class EspecialidadesDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUserGroup, IsAuthenticated]
    queryset = Especialidades.objects.all()
    serializer_class = EspecialidadesSerializer

class DoctoresEspecialidadesListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = DoctoresEspecialidades.objects.all()
    serializer_class = DoctoresEspecialidadesSerializer

class DoctoresEspecialidadesDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUserGroup, IsAuthenticated]
    queryset = DoctoresEspecialidades.objects.all()
    serializer_class = DoctoresEspecialidadesSerializer