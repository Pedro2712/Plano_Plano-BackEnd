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

import funcoes as fc

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
        print(new_Terreno_data)
        # nomeTerreno       = new_Terreno_data['nomeTerreno']
        # codigo            = new_Terreno_data['codigo']
        # gestor            = new_Terreno_data['gestor']
        # cidade            = new_Terreno_data['cidade']
        # zoneamento        = new_Terreno_data['zoneamento']
        # publico           = new_Terreno_data['publico']
        # operacaoUrbana    = new_Terreno_data['operacaoUrbana']
        # nr                = new_Terreno_data['nr']
        
        metragem          = new_Terreno_data['metragem']
        tipoTorre         = new_Terreno_data['tipoTorre']
        quantAndar        = new_Terreno_data['quantAndar']
        quantApartAndar   = new_Terreno_data['quantApartAndar']
        quantTorre        = new_Terreno_data['quantTorre1']
        garagem           = new_Terreno_data['garagem']
        numVagas          = new_Terreno_data['numVagas']
        quantAndarGaragem = new_Terreno_data['quantAndarGaragem']
        fachada           = new_Terreno_data['fachada']
        tipovaga          = new_Terreno_data['tipovaga']
        user              = request.user
        
        eficiencia, coef_aprov = fc.funcao([tipoTorre], [int(quantApartAndar)], [int(quantAndar)], 
                                            [int(quantTorre)], metragem, int(fachada), garagem, 
                                            int(numVagas), tipovaga, int(quantAndarGaragem))

        print(eficiencia, coef_aprov)
        
        # print(funcao(['ODS 4 Plus'], [10], [2], [18], 4476, 0, 'não há', 0, 'não há', 0))
        
        # andarNr          = new_Terreno_data['andarNr']
        # NumAndarNr       = new_Terreno_data['NumAndarNr']
        # quantNr          = new_Terreno_data['quantNr']
        # ca               = new_Terreno_data['ca']
        # eficiencia       = new_Terreno_data['eficiencia']

        # Terrenos = Terreno(nomeTerreno='', codigo='', metragem= metragem, zoneamento='',
        #                    publico='', gestor='', torre=tipoTorre, andares='', numAndar='', quantTorre=quantTorre,
        #                    garagem=garagem, numVagas=numVagas, numMotos='', andaresGaragem='', metragemMall='',
        #                    andaresMall='', andarNr='', NumAndarNr='', quantNr='', ca=coef_aprov, eficiencia=eficiencia, 
        #                    user= user)
        # Terrenos.save()
    #     return Response(status=200)
    # else:
    #     return HttpResponseForbidden()
        # area_equivalente(torre, quanto_por_andar, quantTorre, num_andares, lazer_externo, área_terreno, área_mall, vagas_ed_garagem)
        return Response([round(eficiencia, 3), round(coef_aprov, 3)], status=200)