from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import Order
from .serializers import OrderSerializers
from rest_framework.permissions import AllowAny


class OrderViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    permission_classes = [AllowAny]

