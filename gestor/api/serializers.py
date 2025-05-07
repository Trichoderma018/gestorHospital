from .models import Pacientes, Doctores, Especialidades, Citas, DoctoresEspecialidades
from rest_framework import serializers

class PacientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacientes
        fields = '__all__'

class DoctoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctores
        fields = '__all__'

class EspecialidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidades
        fields = '__all__'

class CitasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citas
        fields = '__all__'

class DoctoresEspecialidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctoresEspecialidades
        fields = '__all__'


