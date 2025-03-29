from django.contrib import admin
from .models import Category, Gadget, Customer


# Register your models here.
admin.site.register(Category)


@admin.register(Gadget)
class GadgetAdmin(admin.ModelAdmin):
    search_fields = ['gadget_name', 'detail_description']
    list_filter = ('status', 'created_on')


admin.site.register(Customer)