# 
from django.urls import path
from . import views


urlpatterns = [
    

  
    path('lista/', views.lista_entradas, name='lista_entradas'),  # Lista de entradas
    path('crear/', views.crear_entrada, name='crear_entrada'),  # Formulario para crear entrada
    path('borrar/<int:entrada_id>/', views.borrar, name='borrar'),


]