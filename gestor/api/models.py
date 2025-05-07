from django.db import models

class Pacientes(models.Model):
    cedula = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, blank=False, null=False)
    fecha_nacimiento = models.DateField(blank=False)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    genero = models.CharField(max_length=10)
    grupo_sanguineo = models.CharField(max_length=10)
    historia_clinica = models.TextField(blank=False, null=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Doctores(models.Model):
    nombre = models.CharField(max_length=100,blank=True, null=True)
    apellido = models.CharField(max_length=100)
    anos_experiencia = models.IntegerField()
    doctores_especialidades = models.ManyToManyField('Especialidades', through='DoctoresEspecialidades')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Especialidades(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=False)

    def __str__(self):
        return self.nombre
    
class Citas(models.Model):
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctores, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    motivo_consulta = models.TextField()

    def __str__(self):
        return f"Cita de {self.paciente} con {self.doctor}"
    
class DoctoresEspecialidades(models.Model):
    doctor = models.ForeignKey(Doctores, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidades, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.doctor} - {self.especialidad}"