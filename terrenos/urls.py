from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/terrenos/', views.api_terrenos),
    path('api/token/', views.api_get_token),
]