from django.db import models
from django.contrib.auth.models import User


# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Gadget(models.Model):
    gadget_id = models.IntegerField(default=0)
    gadget_name = models.CharField(max_length=50, default="")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default=1, related_name="gadgets"
        )
    gadget_detail_desc = models.TextField(blank=False)
    price = models.IntegerField(default=0)
    creater = models.ForeignKey(User, on_delete=models.PROTECT, related_name="gadget_create")
    created_on = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    gadget_short_desc = models.TextField(blank=False)

    class Meta:
        ordering = ['gadget_name']

    def __str__(self):
        return f"{self.gadget_name} created by {self.creater} on {self.created_on}"
