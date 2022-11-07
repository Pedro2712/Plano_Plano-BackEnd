from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Terreno
from .serializers import TerrenoSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import Http404, HttpResponseForbidden, JsonResponse
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
# from calculos import *


def index(request):
    return HttpResponse("Olá mundo! Este é o app Terrenos de Tecnologias Web do Insper.")


@api_view(['POST'])
def cadastra(request):
    print(request.data)
    try:
        if request.method == 'POST':
            user       = request.data['username']
            email      = request.data['email']
            password   = request.data['password']
            first_name = request.data['first_name']
            last_name  = request.data['last_name']


            if user== '' or email== '' or password== '' or first_name== '' or last_name== '' or not email.endswith('@al.insper.edu.br'):
                return JsonResponse({"token": ''})
            else:
                user = User.objects.create_user(username=user, email=email, password=password, 
                                                first_name=first_name, last_name=last_name)
                user.save()
                token, created = Token.objects.get_or_create(user=user)
                print('entrou')
                return JsonResponse({"token": token.key})
        else:
            return HttpResponseForbidden()
    except:
        return HttpResponseForbidden()

@api_view(['POST'])
def api_get_token(request):
    print(request.data)
    try:
        if request.method == 'POST':
            username = request.data['username']
            password = request.data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                return JsonResponse({"token":token.key})
            else:
                return JsonResponse({"token":"Não tem acesso"})
    except:
        return HttpResponseForbidden()

@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def api_terrenos(request):
    try:
        terreno = Terreno.objects.all()
    except terreno.DoesTerrenoxist:
        raise Http404()

    if request.method == 'POST':
        new_Terreno_data = request.data
        terreno.title = new_Terreno_data['title']
        terreno.save()
        
    serialized_Terreno = TerrenoSerializer(terreno, many=True)
    return Response(serialized_Terreno.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def adiciona_terreno(request):
    print(request.data)
    if request.method == 'POST':
        new_Terreno_data  = request.data
        nomeTerreno       = new_Terreno_data['nomeTerreno']
        codigo            = new_Terreno_data['codigo']
        gestor            = new_Terreno_data['gestor']
        cidade            = new_Terreno_data['cidade']
        zoneamento        = new_Terreno_data['zoneamento']
        metragem          = new_Terreno_data['metragem']
        publico           = new_Terreno_data['publico']
        operacaoUrbana    = new_Terreno_data['operacaoUrbana']
        tipoTorre         = new_Terreno_data['tipoTorre']
        quantAndar        = new_Terreno_data['quantAndar']
        quantApartAndar   = new_Terreno_data['quantApartAndar']
        quantTorre        = new_Terreno_data['quantTorre1']
        garagem           = new_Terreno_data['garagem']
        numVagas          = new_Terreno_data['numVagas']
        quantAndarGaragem = new_Terreno_data['quantAndarGaragem']
        fachada           = new_Terreno_data['fachada']
        nr                = new_Terreno_data['nr']
        user              = request.user
        
        # andarNr          = new_Terreno_data['andarNr']
        # NumAndarNr       = new_Terreno_data['NumAndarNr']
        # quantNr          = new_Terreno_data['quantNr']
        # ca               = new_Terreno_data['ca']
        # eficiencia       = new_Terreno_data['eficiencia']

    #     Terrenos = Terreno(nomeTerreno=nomeTerreno, codigo=codigo, metragem= metragem, zoneamento=zoneamento,
    #                        publico=publico, gestor=gestor, torre=torre, andares=andares, numAndar=numAndar, quantTorre=quantTorre,
    #                        garagem=garagem, numVagas=numVagas, numMotos=numMotos, andaresGaragem=andaresGaragem, metragemMall=metragemMall,
    #                        andaresMall=andaresMall, andarNr=andarNr, NumAndarNr=NumAndarNr, quantNr=quantNr, ca=ca, eficiencia=eficiencia, 
    #                        user= user)
    #     Terrenos.save()
    #     return Response(status=200)
    # else:
    #     return HttpResponseForbidden()
        # area_equivalente(torre, quanto_por_andar, quantTorre, num_andares, lazer_externo, área_terreno, área_mall, vagas_ed_garagem)
        return Response(status=200)

# {'nomeTerreno': 'teste', 'codigo': 23, 'gestor': 'Adriano Engel', 'cidade': 'São Paulo', 'zoneamento': 'ZEU', 'metragem': 232, 'publico': 'HMP',
# 'operacaoUrbana': 'Não tem', 'tipoTorre': 'Eng 1', 'quantAndar': 123, 'quantApartAndar': 8, 'quantTorr1': 123, 'garagem': 'Edifício Garagem', 
# 'numVagas': 123, 'quantAndarGaragem': 123, 'fachada': '123', 'nr': 'Sim'}

# title        
# nomeTerreno  
# codigo        
# metragem      
# zoneamento   
# publico      
# gestor       
# torre        
# andares       
# numAndar      
# quantTorre    
# garagem      
# numVagas      
# numMotos      
# andaresGaragem
# metragemMall  
# andaresMall   
# andarNr       
# NumAndarNr    
# quantNr       
# ca      
# eficiencia