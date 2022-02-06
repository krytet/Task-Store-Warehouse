from django.contrib.auth.models import AbstractUser
from django.db import models

TYPE_USER = (
    ('Client', 'Client'),
    ('Manager', 'Manager'),
    ('Warehouse', 'Warehouse'),
)


class User(AbstractUser):
    type_user = models.CharField(choices=TYPE_USER, default='Client',
                                 max_length=10, verbose_name='Type user')
    url = models.URLField(verbose_name='url domen', blank=True, null=True)
