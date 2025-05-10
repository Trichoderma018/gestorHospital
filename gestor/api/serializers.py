from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError # Se le da otro nombre para evitar confusiones porque hay otra función que se llama igual pero hace otra cosa
from .models import Pacientes, Doctores, Especialidades, Citas, DoctoresEspecialidades
from django.contrib.auth.models import User
from rest_framework import serializers

#Serializers de me modelos creados por Django
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password_confirm = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True}
        }

    def validate_username(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("El nombre de usuario debe tener al menos 3 caracteres.")

        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Este nombre de usuario ya está en uso.")
        return value
    
    def validate_email(self, value):
        if not '@' in value:
            raise serializers.ValidationError("El correo electrónico no es válido.")

        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este correo electrónico ya está en uso.")
        return value

    def validate(self, data):
        # Verificar que las contraseñas coincidan
        if data.get('password') != data.get('password_confirm'):
            raise serializers.ValidationError({"password_confirm": "Las contraseñas no coinciden."})
        return data

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        try:
            # Validación del sistema Django que utiliza los validadores configurados en settings.py
            validate_password(value)
        except DjangoValidationError as e:
            # Convierte los errores de Django a errores del serializador
            raise serializers.ValidationError(list(e.messages))
        
        return value

    def create(self, validated_data):
        # Eliminar password_confirm ya que no es un campo del modelo User
        validated_data.pop('password_confirm')
        
        # Guardar la contraseña para usarla después
        password = validated_data.pop('password')
        
        # Crear el usuario sin la contraseña
        user = User.objects.create(**validated_data)
        
        # Establecer la contraseña con el método seguro que aplica el hashing
        user.set_password(password)

        cliente_group, created = Group.objects.get_or_create(name='doctor')
        user.groups.add(cliente_group)

        user.save()
        
        return user


    def update(self, instance, validated_data):
        # Eliminar password_confirm ya que no es un campo del modelo User
        if 'password_confirm' in validated_data:
            validated_data.pop('password_confirm')
        
        # Extraer la contraseña si existe
        if 'password' in validated_data:
            password = validated_data.pop('password')
            # Aplicar el hashing a la nueva contraseña
            instance.set_password(password)
        
        # Actualizar los demás campos
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

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
