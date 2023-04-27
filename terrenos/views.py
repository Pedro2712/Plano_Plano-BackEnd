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

# @api_view(['POST'])
# #@permission_classes([IsAuthenticated])
# def adiciona_terreno(request):
#     print("oiiiii")
#     if request.method == 'POST':
#         new_Terreno_data  = request.data
#         print(new_Terreno_data)
        
        # nomeTerreno       = new_Terreno_data['nomeTerreno']
        # codigo            = new_Terreno_data['codigo']
        # gestor            = new_Terreno_data['gestor']
        # cidade            = new_Terreno_data['cidade']
        # zoneamento        = new_Terreno_data['zoneamento']
        # publico           = new_Terreno_data['publico']
        # operacaoUrbana    = new_Terreno_data['operacaoUrbana']
        # nr                = new_Terreno_data['nr']
        
        # metragem          = new_Terreno_data['metragem']
        # tipoTorre         = new_Terreno_data['tipoTorre']
        # quantAndar        = new_Terreno_data['quantAndar']
        # quantApartAndar   = new_Terreno_data['quantApartAndar']
        # quantTorre        = new_Terreno_data['quantTorre1']
        # garagem           = new_Terreno_data['garagem']
        # numVagas          = new_Terreno_data['numVagas']
        # quantAndarGaragem = new_Terreno_data['quantAndarGaragem']
        # fachada           = new_Terreno_data['fachada']
        # tipovaga          = new_Terreno_data['tipovaga']
        # user              = request.user
        
        
        # eficiencia, coef_aprov = fc.funcao(tipoTorre, quantApartAndar, quantAndar, quantTorre, metragem, fachada, garagem, 
        #                                     numVagas, tipovaga, quantAndarGaragem)

        # print(eficiencia, coef_aprov)
        
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
        # eficiencia = 0
        # coef_aprov = 0
        # return Response([round(eficiencia, 3), round(coef_aprov, 3)], status=200)
        # return Response({'success': 'O terreno foi adicionado com sucesso.'}, status=200)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def adiciona_terreno(request):
    if request.method == 'POST':
        new_terreno_data = request.data
        print(new_terreno_data)
        
        gestor = new_terreno_data['gestor']
        codigo = new_terreno_data['codigo']
        nomeTerreno = new_terreno_data['nomeTerreno']
        metragem = new_terreno_data['metragem']
        zoneamento = new_terreno_data['zoneamento']
        publico = new_terreno_data['publico']
        tipoFachadaAtiva = new_terreno_data['tipoFachadaAtiva']
        garagem = new_terreno_data['garagem']
        numVagas = new_terreno_data['numVagas']
        andarGaragem = new_terreno_data['andarGaragem']
        tipoVaga = new_terreno_data['tipoVaga']
        fachadaAtiva = new_terreno_data['fachadaAtiva']
        
        tipoTorre = new_terreno_data['tipoTorre']
        quantAndar = new_terreno_data['quantAndar']
        apartAndar = new_terreno_data['apartAndar']
        quantTorre = new_terreno_data['quantTorre']
        
        
        # # Certifica-se de que todos os campos necessários foram fornecidos na solicitação
        # required_fields = ['metragem', 'tipoTorre', 'quantAndar', 'apartAndar', 'quantTorre', 'garagem', 'numVagas', 'andarGaragem', 'fachada', 'tipovaga']
        # for field in required_fields:
        #     if field not in new_terreno_data:
        #         return Response({'error': f'O campo "{field}" é obrigatório.'}, status=400)
        
        # Calcula a eficiência e coeficiente de aproveitamento do terreno
        eficiencia, coef_aprov = fc.funcao(categoria=tipoTorre, quanto_por_andar=apartAndar,
                                           num_torres=quantTorre, num_andares=quantAndar, area_terreno=metragem,
                                           zoneamento=zoneamento, tipo_garagem=garagem, disp_vagas=tipoVaga,
                                           loc_mall=tipoFachadaAtiva, vagas_garagem=numVagas,
                                           num_andares_garagem=andarGaragem, area_mall=fachadaAtiva)

        # Salva o novo terreno no banco de dados
        print (eficiencia, coef_aprov)
        # user = request.user
        # Terrenos = Terreno(nomeTerreno='', codigo='', metragem=new_terreno_data['metragem'], zoneamento='', publico='', gestor='', 
        #                    torre=new_terreno_data['tipoTorre'], andares='', numAndar='', quantTorre=new_terreno_data['quantTorre'], 
        #                    garagem=new_terreno_data['garagem'], numVagas=new_terreno_data['numVagas'], numMotos='', 
        #                    andaresGaragem='', metragemMall='', andaresMall='', andarNr='', NumAndarNr='', quantNr='', 
        #                    ca=coef_aprov, eficiencia=eficiencia, user=user)
        # Terrenos.save()

        return Response([round(eficiencia, 3), round(coef_aprov, 3)], status=200)
    
    # Se a solicitação não for POST, retorna um erro 405 - Method Not Allowed
    return Response({'error': 'O método solicitado não é permitido.'}, status=405)
