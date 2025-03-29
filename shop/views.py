from django.shortcuts import render
from django.views import generic
from .models import Gadget


# Create your views here.
class GadgetList(generic.ListView):
    queryset = Gadget.objects.all()
    template_name = "shop/index.html"
    paginate_by = 4
