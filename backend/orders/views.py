from .models import *
from .serializers import *
from rest_framework import permissions, renderers, viewsets
from django_filters import rest_framework as filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User




class OrdersViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # def perform_create(self, serializer):
    #     serializer.save(created_by=self.request.user)




class OrderLineViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = OrderLine.objects.all()
    serializer_class = OrderLineSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('order',)