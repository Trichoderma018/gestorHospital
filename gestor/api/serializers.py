from .models import Pacientes, Doctores, Especialidades, Citas, DoctoresEspecialidades
from django.contrib.auth.models import User
from rest_framework import serializers

#Serializers de me modelos creados por Django
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff']

    def validate_username(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("El nombre de usuario debe tener al menos 3 caracteres.")
        return value
    
    def validate_email(self, value):
        if not '@' in value:
            raise serializers.ValidationError("El correo electrónico no es válido.")
        return value
    
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        return value

# Serializers de Modelos creados por el desarrollador
class PacientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacientes
        fields = '__all__'

    def validate_nombre(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("El nombre debe tener al menos 2 caracteres.")
        return value
    
    def validate_apellido(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("El apellido debe tener al menos 2 caracteres.")
        return value
    
    def validate_fecha_nacimiento(self, value):
        # Verificar que la fecha de nacimiento no sea futura
        if value > date.today():
            raise serializers.ValidationError("La fecha de nacimiento no puede ser una fecha futura.")
        
        # Verificar que no sea un paciente extremadamente anciano (más de 120 años)
        edad_max = date.today().year - value.year
        if edad_max > 120:
            raise serializers.ValidationError("La fecha de nacimiento no es válida. La edad resultante es mayor a 120 años.")
        return value
    
    def validate_historia_clinica(self, value):
        if len(value.strip()) < 10:
            raise serializers.ValidationError("La historia clínica debe tener al menos 10 caracteres.")
        return value

class DoctoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctores
        fields = '__all__'
    
    def validate_nombre(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("El nombre debe tener al menos 2 caracteres.")
        return value
    
    def validate_apellido(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("El apellido debe tener al menos 2 caracteres.")
        return value
    
    def validate_anos_experiencia(self, value):
        if value < 0:
            raise serializers.ValidationError("Los años de experiencia no pueden ser negativos.")
        if value > 70:
            raise serializers.ValidationError("Los años de experiencia no pueden ser mayores a 70.")
        return value

class EspecialidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidades
        fields = '__all__'

    def validate_nombre(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("El nombre de la especialidad debe tener al menos 2 caracteres.")
        return value
    
    def validate_descripcion(self, value):
        if len(value.strip()) < 10:
            raise serializers.ValidationError("La descripción de la especialidad debe tener al menos 10 caracteres.")
        return value

class CitasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citas
        fields = '__all__'

    def validate_fecha_hora(self, value):
        # Verificar que la fecha de la cita no sea en el pasado
        if value < datetime.now():
            raise serializers.ValidationError("La fecha y hora de la cita no puede ser en el pasado.")
        return value
    
    def validate_motivo_consulta(self, value):
        if len(value.strip()) < 5:
            raise serializers.ValidationError("El motivo de la consulta debe tener al menos 5 caracteres.")
        return value

class DoctoresEspecialidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctoresEspecialidades
        fields = '__all__'
