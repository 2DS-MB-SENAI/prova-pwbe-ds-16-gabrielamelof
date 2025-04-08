from django.shortcuts import render, redirect
from .models import Medico, Consulta
from .forms import Itemform
from .serializers import ConsultaSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
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

@api_view(['GET'])

def detalhes_consulta(request, pk):
    try: 
        consulta = Consulta.objects.get(pk=pk)
    except Consulta.DoesNotExist:
        return Response({'erro': 'Consulta não cadastrada'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ConsultaSerializer(consulta)
    return Response(serializer.data)