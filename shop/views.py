from django.shortcuts import render
from django.views import generic
from .models import Gadget, Category


# Create your views here.
class GadgetList(generic.ListView):
    queryset = Gadget.objects.all()
    template_name = "shop/index.html"
    paginate_by = 4


def category(request, dl):
    # Grab the category from the url
    category = Category.objects.get(category_name=dl)
    gadgets = Gadget.objects.filter(category=category)
    return render(request, 'shop/category.html', {'gadgets': gadgets, 'category': category})