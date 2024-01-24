from django.shortcuts import render, get_object_or_404
from bichinhos.models import Item, Tag


def index(request):
  animais = Item.objects.filter(publicada=True)
  tags = Tag.objects.all()
  selected_tag = request.GET.get('tags', None)
  if selected_tag:
    animais = animais.filter(tags__name=selected_tag)

  context = {'cards': animais, 'tags': tags, 'selected_tag': selected_tag}
  return render(request, 'galeria/index.html', context)

def imagem(request, foto_id):
  animais = get_object_or_404(Item, pk=foto_id)
  return render(request, 'galeria/imagem.html', {"f": animais})

def nossa_missao(request):
  return render(request, 'galeria/nossa_missao.html')

def sobre(request):
  return render(request,'galeria/sobre.html')