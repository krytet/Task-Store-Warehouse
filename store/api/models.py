from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


STATUS_ORDER = (
    (1, 'Created'),
    (2, 'Accepted'),
    (3, 'Being formed'),
    (4, 'Awaiting shipment'),
    (5, 'Shipped'),
    (6, 'Waiting at the pick-up point'),
    (7, 'Completed'),
)


class Order(models.Model):
    warehouse = models.ForeignKey(User, on_delete=models.PROTECT,
                                  related_name='orders',
                                  limit_choices_to={'type_user': 'Warehouse'},
                                  verbose_name='warehouse')
    status = models.IntegerField(choices=STATUS_ORDER,
                                 verbose_name='Status order')

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['-id']

    def __str__(self):
        return f'{self.id} - {self.status}'
