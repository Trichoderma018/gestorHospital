from django.db import models

#class User(models.Model):
#como hago para usar el model User de django.contrib.auth.models?
# o tengo que crear un nuevo modelo?

class Pacientes(models.Model):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro')
    ]
    
    GRUPO_SANGUINEO_CHOICES = [
        ('A+', 'A positivo'),
        ('A-', 'A negativo'),
        ('B+', 'B positivo'),
        ('B-', 'B negativo'),
        ('AB+', 'AB positivo'),
        ('AB-', 'AB negativo'),
        ('O+', 'O positivo'),
        ('O-', 'O negativo')
    ]
    
    cedula = models.CharField(max_length=20, unique=True, null=False, blank=False)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    apellido = models.CharField(max_length=100, blank=False, null=False)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES, null=False, blank=False)
    grupo_sanguineo = models.CharField(max_length=3, choices=GRUPO_SANGUINEO_CHOICES, blank=False, null=False)
    historia_clinica = models.TextField(blank=False, null=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Doctores(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    apellido = models.CharField(max_length=100, blank=False, null=False)
    anos_experiencia = models.IntegerField(null=False, blank=False)
    doctores_especialidades = models.ManyToManyField('Especialidades', through='DoctoresEspecialidades')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Especialidades(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.nombre
    
class Citas(models.Model):
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctores, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField(null=False, blank=False)
    motivo_consulta = models.TextField(null=False, blank=False)

    def __str__(self):
        return f"Cita de {self.paciente} con {self.doctor}"
    
class DoctoresEspecialidades(models.Model):
    doctor = models.ForeignKey(Doctores, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidades, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.doctor} - {self.especialidad}"