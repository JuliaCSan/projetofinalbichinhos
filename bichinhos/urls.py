from django.urls import path

from bichinhos import views
from bichinhos.views import index, imagem, buscar_por_tag

urlpatterns = [
    path('', views.index, name='index'),
    path('imagem/<int:foto_id>/', imagem, name='imagem')
    path('buscar_por_tag/<str:tag>/', buscar_por_tag, name='buscar_por_tag'),
]