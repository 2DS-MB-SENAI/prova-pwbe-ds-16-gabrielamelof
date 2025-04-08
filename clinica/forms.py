from django import forms
from .models import Consulta


class Itemform(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'