from rest_framework import serializers

from cadastro.models import Caieirasfy

class CadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caieirasfy
        fields = ('nome_musica', 'artista', 'genero', 'link_musica'),