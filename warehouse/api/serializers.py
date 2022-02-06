from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Order

User = get_user_model


class OrderSerializers(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
