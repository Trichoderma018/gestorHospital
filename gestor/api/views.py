from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import pacientes, doctores, citas, especialidades, doctores_especialidades
from .serializers import PacientesSerializer, DoctoresSerializer, CitasSerializer, EspecialidadesSerializer, DoctoresEspecialidadesSerializer

class PacientesListCreateView(ListCreateAPIView):
    queryset = pacientes.objects.all()
    serializer_class = PacientesSerializer

class PacientesDetailView(RetrieveUpdateDestroyAPIView):
    queryset = pacientes.objects.all()
    serializer_class = PacientesSerializer

class DoctoresListCreateView(ListCreateAPIView):
    queryset = doctores.objects.all()
    serializer_class = DoctoresSerializer

class DoctoresDetailView(RetrieveUpdateDestroyAPIView):
    queryset = doctores.objects.all()
    serializer_class = DoctoresSerializer

class CitasListCreateView(ListCreateAPIView):
    queryset = citas.objects.all()
    serializer_class = CitasSerializer

class CitasDetailView(RetrieveUpdateDestroyAPIView):
    queryset = citas.objects.all()
    serializer_class = CitasSerializer

class EspecialidadesListCreateView(ListCreateAPIView):
    queryset = especialidades.objects.all()
    serializer_class = EspecialidadesSerializer

class EspecialidadesDetailView(RetrieveUpdateDestroyAPIView):
    queryset = especialidades.objects.all()
    serializer_class = EspecialidadesSerializer

class DoctoresEspecialidadesListCreateView(ListCreateAPIView):
    queryset = doctores_especialidades.objects.all()
    serializer_class = DoctoresEspecialidadesSerializer

class DoctoresEspecialidadesDetailView(RetrieveUpdateDestroyAPIView):
    queryset = doctores_especialidades.objects.all()
    serializer_class = DoctoresEspecialidadesSerializer
