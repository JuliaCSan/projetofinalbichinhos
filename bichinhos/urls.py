from django.urls import path

from bichinhos import views
from bichinhos.views import index, imagem

urlpatterns = [
    path('', views.index, name='index'),
    path('imagem/<int:foto_id>/', imagem, name='imagem'),
    path('nossa_missao',views.nossa_missao,name='nossa_missao'),
    path('sobre',views.sobre,name='sobre')
]