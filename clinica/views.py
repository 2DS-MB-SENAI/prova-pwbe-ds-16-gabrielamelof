from django.shortcuts import render, redirect
from .models import Medico, Consulta
from .forms import Itemform

# Create your views here.
def listar_medicos(request):
    if request.method == "POST":
        medico = busca_especialidade(request)
    else:
        medico = []
    medicos = Medico.objects.all()
    return render(request, 'clinica/listar_medicos.html', {'medicos': medicos, 'medico': medico})


def criar_consulta(request):
    if request.method == 'POST':
        form = Itemform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_medicos')
    else:
        form = Itemform()
        
    
    return render(request, 'clinica/form_consulta.html', {'form' : form})


def busca_especialidade(request):
    especialidade = request.POST.get('especialidade_filtro')
    print(especialidade)
    medico = Medico.objects.filter(especialidade__icontains = especialidade)
    return medico