# Generated by Django 4.2.19 on 2025-04-02 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_renting_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='renting',
            name='status',
            field=models.IntegerField(choices=[(0, 'peding'), (1, 'complete')], default=0),
        ),
    ]
