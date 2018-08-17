from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from itertools import chain
from .models import Lost, Found
from .serializers import *
from .filters import Filter


class LostViewSet(viewsets.ModelViewSet):            
    """
    API endpoint that allows Losts to be viewed.
    """
    queryset = Lost.objects.all().order_by('date')
    serializer_class = LostSerializer
    filter_class = Filter


class FoundViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Founds to be viewed.
    """   
    queryset = Found.objects.all().order_by('date')
    serializer_class = FoundSerializer
    filter_class = Filter


class SpamViewSet(viewsets.ViewSet):
    """
    API endpoint that allows Spams to be viewed.
    """
    def list(self, request):      
        LostSpamList = Lost.objects.all().filter(item_is_spam=True)       # Extracts Lost spam entities
        FoundSpamList = Found.objects.all().filter(item_is_spam=True)     # Extracts Found spam entities
        queryset = list(chain(LostSpamList,FoundSpamList))                # Combines above two lists
        serializer = SpamSerializer(queryset, many= True)
        return Response(serializer.data)

