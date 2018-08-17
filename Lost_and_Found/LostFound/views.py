from django.shortcuts import render
from .models import Lost, Found
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from itertools import chain

class LostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Losts to be viewed.
    """
    queryset = Lost.objects.all().order_by('date')
    serializer_class = LostSerializer


class FoundViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Founds to be viewed.
    """
    queryset = Found.objects.all().order_by('date')
    serializer_class = FoundSerializer


class SpamViewSet(viewsets.ViewSet):
    """
    API endpoint that allows Lost Spams to be viewed.
    """
    def list(self, request):
        FoundSpamList = Found.objects.all().filter(item_is_spam=True)
        LostSpamList = Lost.objects.all().filter(item_is_spam=True)
        queryset = list(chain(FoundSpamList,LostSpamList))
        serializer = TitleSerializer(queryset, many= True)
        return Response(serializer.data)
        