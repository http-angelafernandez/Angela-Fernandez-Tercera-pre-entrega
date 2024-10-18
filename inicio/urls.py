
from django.urls import path 
from inicio.views import inicio, crear_libro, buscar_libro

urlpatterns = [
    path('', inicio, name='inicio'),
    path('crear-libro/<str:nombre>/<str:genero>/<int:autor>/', crear_libro, name='crear_libro'),
    path('buscar-libro/', buscar_libro, name='buscar_libro'),
    path('crear-libro/', crear_libro, name='crear_libro')


    ]