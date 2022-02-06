from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import Order
from .permissions import IsWarehouseOrReadOnly
from .serializers import OrderSerializers


class OrderViewSet(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    permission_classes = [IsWarehouseOrReadOnly]
