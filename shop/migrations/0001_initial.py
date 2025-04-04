# Generated by Django 4.2.19 on 2025-03-28 06:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Gadget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gadget_id', models.IntegerField(unique=True)),
                ('gadget_name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('detail_description', models.TextField()),
                ('intended_use', models.CharField(max_length=300)),
                ('warning', models.TextField(default='No warning', max_length=200)),
                ('minimum_usage_age', models.IntegerField(default='18')),
                ('unit_rent_price', models.IntegerField(default=0)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('short_description', models.TextField()),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='gadgets', to='shop.category')),
                ('creater', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='gadget_created', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['gadget_name'],
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=250)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
