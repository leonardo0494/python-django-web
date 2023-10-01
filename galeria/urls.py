from django.urls import path
from galeria.views import *

urlpatterns = [
    path('', index, name="home"),
    path('imagem', imagem, name="imagem")
]
