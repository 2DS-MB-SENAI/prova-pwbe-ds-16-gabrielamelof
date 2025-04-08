from django.db import models
from django.core.validators import MaxValueValidator
from datetime import date
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=2,unique=True)
    address = models.TextField(null=True, blank=True)
    birth_date = models.DateField(validators=[MaxValueValidator(date.today())], blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    
    def __str__(self):
        return self.username