from django.contrib import admin
from .models import Category, Gadget, Customer, Renting
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
admin.site.register(Category)


@admin.register(Gadget)
class GadgetAdmin(SummernoteModelAdmin):
    list_display = ('id', 'gadget_name', 'gadget_id', 'slug', 'minimum_usage_age', 'status')
    search_fields = ['gadget_id', 'gadget_name', 'detail_description']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('gadget_name',)}
    summernote_fields = ('detail_description', 'warning', 'short_description')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'first_name', 'last_name', 'age')
    search_fields = ['last_name']
    list_filter = ('age',)


@admin.register(Renting)
class RentingAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'gadget', 'first_name', 'last_name', 'status')
    search_fields = ['customer', 'gadget']
    list_filter = ('status', 'created_on', 'customer')