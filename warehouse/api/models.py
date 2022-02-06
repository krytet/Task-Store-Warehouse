from django.db import models

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
    id = models.IntegerField(verbose_name='ID', primary_key=True)
    warehouse = models.IntegerField(verbose_name='ID User')
    status = models.IntegerField(choices=STATUS_ORDER,
                                 verbose_name='Status order')

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['-id']

    def __str__(self):
        return f'{self.id} - {self.status}'
