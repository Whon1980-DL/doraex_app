from django.db import models
from django.contrib.auth.models import User


# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Gadget(models.Model):
    gadget_id = models.IntegerField(unique=True)
    gadget_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, related_name="gadgets")
    detail_description = models.TextField(blank=False)
    intended_use = models.CharField(max_length=300, blank=False)
    warning = models.TextField(max_length=200, default="No warning")
    minimum_usage_age = models.IntegerField(default="18")
    unit_rent_price = models.IntegerField(default=0)
    creater = models.ForeignKey(User, on_delete=models.PROTECT, related_name="gadget_created")
    created_on = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    short_description = models.TextField(blank=False)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['gadget_name']

    def __str__(self):
        return f"{self.gadget_name} created by {self.creater} on {self.created_on}"


class Customer(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    age = models.IntegerField(blank=False, default="18")
    phone = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=250)
    shipping_address = models.TextField(blank=False, default="")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}|age {self.age}"

