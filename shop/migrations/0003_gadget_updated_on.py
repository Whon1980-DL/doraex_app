# Generated by Django 4.2.19 on 2025-03-29 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_customer_age_customer_shipping_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='gadget',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
