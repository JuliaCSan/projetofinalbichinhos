from django.shortcuts import render, get_object_or_404
from bichinhos.models import Item


def index(request):
  animais = Item.objects.filter(publicada=True)
  return render(request, 'galeria/index.html', {"cards": animais})



def imagem(request, foto_id):
  animais = get_object_or_404(Item, pk=foto_id)
  return render(request, 'galeria/imagem.html', {"f": animais})

def buscar_por_tag(request, tag):
  objetos = Item.objects.filter(tags__icontains=tag)
  return render(request, 'galeria/busca_por_tag.html', {'objetos': objetos, 'tag': tag})