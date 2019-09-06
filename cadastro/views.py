from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from cadastro.models import Caieirasfy
from cadastro.serializers import CadastroSerializer


class CaieirasfyViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['^nome_musica', '^artista', '^genero', '^link_musica']
    queryset = Caieirasfy.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = CadastroSerializer
