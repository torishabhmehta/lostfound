from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from itertools import chain
from .models import Lost, Found
from .serializers import *
from .filters import *


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


