from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator
from datetime import date
from django.utils import timezone
# Create your models here.
class Medico(models.Model):
    nome = models.CharField(max_length=255, validators=[MinLengthValidator(5)])
    escolhas_especialidade = (
        ('ORTOPEDIA', 'Ortopedia'),
        ('DERMATOLOGIA', 'Dermatologia'), 
        ('CAR', 'CAR'), 
        ('OFTALMOLOGIA', 'Oftalmologia'),
    )
    especialidade = models.CharField(max_length=20, choices=escolhas_especialidade)
    crm = models.CharField(max_length=8, unique=True)
    email = models.EmailField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nome
    
class Consulta(models.Model):
    paciente = models.CharField(max_length=255)
    data = models.DateTimeField(
        validators=[
            MinValueValidator(timezone.now()),
        ]
    )

    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    escolhas_status = (
        ('AGENDADO', 'Agendado'), 
        ('REALIZADO', 'Realizado'), 
        ('CANCELADO', 'Cancelado'), 
    )
    status = models.CharField(max_length=20, choices=escolhas_status)

    def __str__(self):
        return self.paciente
