# Generated by Django 4.2.19 on 2025-04-01 21:36

import datetime
from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_renting_customer_alter_renting_gadget'),
    ]

    operations = [
        migrations.AlterField(
            model_name='renting',
            name='end_date',
            field=models.DateField(default=datetime.date.today, validators=[shop.models.Renting.Date_validation]),
        ),
        migrations.AlterField(
            model_name='renting',
            name='start_date',
            field=models.DateField(default=datetime.date.today, validators=[shop.models.Renting.Date_validation]),
        ),
    ]
