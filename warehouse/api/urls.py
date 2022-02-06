from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import OrderViewSet

router = DefaultRouter()
router.register('orders', OrderViewSet, 'orders')


urlpatterns = [
    path('', include(router.urls))
]
