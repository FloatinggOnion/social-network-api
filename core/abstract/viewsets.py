from rest_framework import viewsets
from rest_framework import filters

class AbstractViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['updated', 'created']    # List of fields that can be used as ordering params
    ordering = ['-updated']     # Put the more recently updated ones first, then others