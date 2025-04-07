from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from datetime import date, timedelta
from django.core.exceptions import ValidationError


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
    featured_image = CloudinaryField('image', default='default')
    detail_description = models.TextField(blank=False)
    intended_use = models.CharField(max_length=300, blank=False)
    warning = models.CharField(max_length=2000, default="No warning")
    minimum_usage_age = models.IntegerField(default="18")
    unit_rent_price = models.IntegerField(default=0)
    creater = models.ForeignKey(User, on_delete=models.PROTECT, related_name="gadget_created")
    created_on = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    short_description = models.CharField(blank=False)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['gadget_name']

    def __str__(self):
        return self.gadget_name


class Customer(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    age = models.IntegerField(blank=False, default="18")
    phone = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=250)
    shipping_address = models.CharField(max_length=2000, blank=False, default="")
    
    def __str__(self):
        return f"{self.id} {self.first_name} {self.last_name}|age {self.age} {self.customer} "


STATUS = ((0, "peding"), (1, "complete"))


class Renting(models.Model):

    def Date_validation(value):
        if value < date.today():
            raise ValidationError("The date cannot be in the past")
        
    gadget = models.ForeignKey(Gadget, on_delete=models.CASCADE, related_name="renting_item")
    quantity = models.PositiveIntegerField(default="", blank=False)
    price = models.IntegerField(default=0)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="renter")
    first_name = models.CharField(max_length=50, blank=False, default="")
    last_name = models.CharField(max_length=50, blank=False, default="")
    start_date = models.DateField(default=date.today, validators=[Date_validation])
    end_date = models.DateField(default=date.today, validators=[Date_validation])
    number_days_rent = models.PositiveIntegerField(default="", blank=False)
    address = models.CharField(max_length=300, default="", blank=False)
    email = email = models.EmailField(default="", max_length=250)
    phone = models.CharField(max_length=30, default="", blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateField(default=date.today)

    def __str__(self):
        return f"renting id:{self.id} {self.customer} rent {self.quantity} {self.gadget} from {self.start_date} unitl {self.end_date}"

    @property
    def Total_price(self):
        total_price = self.price * self.quantity * self.number_days_rent
        return total_price
    
    
