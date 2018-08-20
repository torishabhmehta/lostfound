from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet

# Filter set for normal viewsets

class Filter(FilterSet):
    filter_backends = (SearchFilter, DjangoFilterBackend,)
    search_fields = ('item_name', 'item_desc')
    filter_fields = ('item_category',)
