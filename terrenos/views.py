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


def index(request):
    return HttpResponse("Olá mundo! Este é o app Terrenos de Tecnologias Web do Insper.")

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def api_terrenos(request):
    try:
        terreno = Terreno.objects.all()
    except terreno.DoesTerrenoxist:
        raise Http404()

    if request.method == 'POST':
        new_note_data = request.data
        terreno.title = new_note_data['title']
        terreno.save()
        
    serialized_Terreno = TerrenoSerializer(terreno, many=True)
    return Response(serialized_Terreno.data)

@api_view(['POST'])
def api_get_token(request):
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