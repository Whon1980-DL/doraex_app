from django.contrib import admin
from .models import Category, Gadget, Customer, Renting


# Register your models here.
admin.site.register(Category)


@admin.register(Gadget)
class GadgetAdmin(admin.ModelAdmin):
    """
    Lists fields for display in admin, fileds for search,
    field filters and fields to prepopulate.
    """
    list_display = ('gadget_id', 'gadget_name', 'category', 'unit_rent_price',
                    'minimum_usage_age',)
    search_fields = ['gadget_id', 'gadget_name', 'detail_description']
    list_filter = ('status', 'minimum_usage_age')
    prepopulated_fields = {'slug': ('gadget_name',)}


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """
    Lists fields for display in admin, fileds
    for search and field filters.
    """
    list_display = ('id', 'customer', 'first_name', 'last_name', 'age')
    search_fields = ['last_name']
    list_filter = ('age',)


@admin.register(Renting)
class RentingAdmin(admin.ModelAdmin):
    """
    Lists fields for display in admin, fileds
    for search and field filters.
    """
    list_display = ('id', 'customer', 'gadget', 'first_name',
                    'last_name', 'status')
    search_fields = ['customer', 'gadget']
    list_filter = ('status', 'created_on', 'customer')
