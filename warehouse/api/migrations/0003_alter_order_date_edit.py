# Generated by Django 4.0.2 on 2022-02-06 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_order_options_order_date_edit_alter_order_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_edit',
            field=models.DateTimeField(editable=False, verbose_name='Time last edit'),
        ),
    ]
