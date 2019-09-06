from django.db import models

# Create your models here.

class Caieirasfy(models.Model):
    nome_musica = models.CharField(
        max_length = 255,
    )

    artista = models.CharField(
        max_length = 255,
    )

    genero = models.CharField(
        max_length = 255,
    )

    link_musica = models.CharField(
        max_length = 255,
    )

    def __str__(self):
        return 'A música atual é: ' + self.nome_musica + ', o artista é ' + self.artista + ', o gênero musical é: ' + self.genero + '. Acesse o link da música! ' + self.link_musica