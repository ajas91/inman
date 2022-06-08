from .models import *
from .serializers import *
from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


class CustomersViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomersSerializer
    
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            phone_number = serializer.data.get('phone_number')
            address = serializer
            customer = Customer(name=name,phone_number=phone_number,address=address)
            customer.save()

        print(serializer.errors)        
    # def perform_create(self, serializer):
    #     serializer.save(created_by=self.request.user)


# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     This viewset automatically provides `list` and `retrieve` actions.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer