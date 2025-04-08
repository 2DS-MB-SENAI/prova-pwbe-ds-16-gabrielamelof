from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import	CustomUser
from django.contrib.auth import authenticate

# Create your views here.

@api_view(['POST'])
def criar_usuario(request):
    username = request.data.get('username')
    password = request.data.get('password')
    phone = request.data.get('phone')
    


    if not username or not password:
        return Response({'Erro' : f'Campos incompletos'}, status= status.HTTP_400_BAD_REQUEST)
    if CustomUser.objects.filter(username=username).exists():
        return Response({'Erro': f'Username {username} já existe'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = CustomUser.objects.create_user(
        username = username, 
        password = password,
        phone = phone
    )
    return Response({'Mensagem': f'Usuário {username} criado com sucesso'}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logar_usuario(request):
    return Response({"Mensagem":"Olá, Usuário!"}, status=status.HTTP_200_OK)