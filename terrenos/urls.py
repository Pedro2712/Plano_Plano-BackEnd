from django.urls import path

from . import views

urlpatterns = [
    path('cadastra/', views.cadastra),
    path('api/token/', views.api_get_token),
    path('api/terrenos/', views.api_terrenos),
    path('adiciona/terreno/', views.adiciona_terreno),
]