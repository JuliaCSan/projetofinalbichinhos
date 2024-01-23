from django.db import models

class Item(models.Model):
    OPCOES_CATEGORIA = [
        ("", ""),
        ("GATO", "Gato"),
        ("CACHORRO", "Cachorro"),
        ("MACHO", "Macho"),
        ("FEMEA", "Fêmea"),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=50, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d", blank=False)
    publicada = models.BooleanField(default=False)
    def __str__(self):
        return self.nome