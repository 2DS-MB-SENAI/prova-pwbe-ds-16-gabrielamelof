from django.shortcuts import render
from .models import Servico, Agendamento
from .serializers import ServicoSerializer, AgendamentoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.
@api_view(['GET', 'POST'])
def servicos(request):
    if request.method == 'GET':
        servicos = Servico.objects.all()
        serializer = ServicoSerializer(servicos, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ServicoSerializer(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def agendamentos(request):
    if request.method == 'GET':
        agendamentos = Agendamento.objects.all()
        serializer = ServicoSerializer(agendamentos, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = AgendamentoSerializer(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# @api_view(['POST'])
# def create_servico(request):
#     if request.method == 'POST':
#         serializer = ServicoSerializer(data=request.data, many=isinstance(request.data, list))
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# @api_view(['POST'])
# def create_agendamento(request):
#     if request.method == 'POST':
#         serializer = AgendamentoSerializer(data=request.data, many=isinstance(request.data, list))
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def pegar_servico(request, pk):
    try:
        evento = Servico.objects.get(pk=pk)
    except Servico.DoesNotExist:
        return Response({'erro':'Serviço não cadastrado'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ServicoSerializer(evento)
    return  Response(serializer.data)

@api_view(['GET'])
def pegar_agendamento(request, pk):
    try:
        evento = Agendamento.objects.get(pk=pk)
    except Agendamento.DoesNotExist:
        return Response({'erro':'Agendamento não cadastrado'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = AgendamentoSerializer(evento)
    return  Response(serializer.data)