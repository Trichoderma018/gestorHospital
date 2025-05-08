from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Pacientes, Doctores, Citas, Especialidades, DoctoresEspecialidades
from .serializers import PacientesSerializer, DoctoresSerializer, CitasSerializer, EspecialidadesSerializer, DoctoresEspecialidadesSerializer

class PacientesListCreateView(ListCreateAPIView):
    queryset = Pacientes.objects.all()
    serializer_class = PacientesSerializer

class PacientesDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Pacientes.objects.all()
    serializer_class = PacientesSerializer

class DoctoresListCreateView(ListCreateAPIView):
    queryset = Doctores.objects.all()
    serializer_class = DoctoresSerializer

class DoctoresDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Doctores.objects.all()
    serializer_class = DoctoresSerializer

class CitasListCreateView(ListCreateAPIView):
    queryset = Citas.objects.all()
    serializer_class = CitasSerializer

class CitasDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Citas.objects.all()
    serializer_class = CitasSerializer

class EspecialidadesListCreateView(ListCreateAPIView):
    queryset = Especialidades.objects.all()
    serializer_class = EspecialidadesSerializer

class EspecialidadesDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Especialidades.objects.all()
    serializer_class = EspecialidadesSerializer

class DoctoresEspecialidadesListCreateView(ListCreateAPIView):
    queryset = DoctoresEspecialidades.objects.all()    # Cambiado de Doctores_especialidades a DoctoresEspecialidades
    serializer_class = DoctoresEspecialidadesSerializer

class DoctoresEspecialidadesDetailView(RetrieveUpdateDestroyAPIView):
    queryset = DoctoresEspecialidades.objects.all()    # Cambiado de Doctores_especialidades a DoctoresEspecialidades
    serializer_class = DoctoresEspecialidadesSerializer