from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from ..models import BreakdownLog, Machine, Type, Brand, Category, Location, Supplier
from .serializers import BreakdownLogSerializer, MachineSerializer, TypeSerializers, BrandSerializers, CategorySerializers, SupplierSerializers
from rest_framework.exceptions import ValidationError
from django_filters.rest_framework import DjangoFilterBackend
from ..filters import MachineFilter
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from permissions.base_permissions import IsAdmin, IsHR, IsMechanic, IsSupervisor, IsAdminOrSupervisorOrMechanic, IsAdminOrMechanic


class MachinePagination(PageNumberPagination):
    page_size = 10  # Number of items per page
    page_size_query_param = 'page_size'  # Allows users to specify the page size via query parameter
    max_page_size = 100  # Maximum number of items per page


class MachineViewSet(ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = MachineFilter
    ordering_fields = '__all__'  # Allows ordering on all fields
    ordering = ['machine_id']  # Default ordering (optional)
    pagination_class = MachinePagination

    # def get_permissions(self):
    #     if self.action in ['list', 'retrieve']:
    #         # print(f"{self.action.capitalize()} called.")
    #         return [IsAdminOrSupervisorOrMechanic()]
        
    #     if self.action in ['create', 'update', 'partial_update', 'destroy']:
    #         # print(f"{self.action} called.")
    #         return [IsAdminOrMechanic()]  # Adjust as needed
        
    #     return super().get_permissions()


    
class BreakdownLogViewSet(ModelViewSet):
    queryset = BreakdownLog.objects.all()
    serializer_class = BreakdownLogSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'create', 'update', 'partial_update', 'destroy']:
            return [IsAdmin()]  # Adjust as needed   
        return super().get_permissions()

class TypeViewSet(ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializers

class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializers

class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializers



class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

