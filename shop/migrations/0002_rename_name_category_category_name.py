# Generated by Django 4.2.19 on 2025-03-26 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='category_name',
        ),
    ]
