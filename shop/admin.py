from django.contrib import admin
from .models import Category, Gadget, Customer


# Register your models here.
admin.site.register(Category)


@admin.register(Gadget)
class GadgetAdmin(admin.ModelAdmin):
    list_display = ('gadget_name', 'gadget_id', 'slug', 'minimum_usage_age', 'status')
    search_fields = ['gadget_id', 'gadget_name', 'detail_description']
    list_filter = ('status', 'created_on')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age')
    search_fields = ['last_name']
    list_filter = ('age',)
