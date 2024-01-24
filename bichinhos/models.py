from django.db import models



class Tag(models.Model):
    name = models.CharField(max_length=100,null=False, blank=False)
    def __str__(self):
       return f"{self.name}"
class Item(models.Model):
    OPCOES_CATEGORIA = [
        ("GATO","Gato"),
        ("CACHORRO", "Cachorro"),
        ("MACHO", "Macho"),
        ("FEMEA", "Femea")
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=50, null=False,choices=OPCOES_CATEGORIA,blank=False,default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d", blank=False)
    publicada = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.nome}"