from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Gadget, Category


# Create your views here.
class GadgetList(generic.ListView):
    queryset = Gadget.objects.filter(status=1)
    template_name = "shop/index.html"
    paginate_by = 4


def category(request, dl):
    # Grab the category from the url
    category = Category.objects.get(category_name=dl)
    gadgets = Gadget.objects.filter(category=category, status=1)
    return render(request, 'shop/category.html', {'gadgets': gadgets, 'category': category})


def gadget_view(request, slug):
    """
    Display an individual :model:`shop.Gadget`.

    **Context**

    ``gadget``
        An instance of :model:`shop.Gadget`.

    **Template:**

    :template:`shop/gadget_view.html`
    """

    queryset = Gadget.objects.filter(status=1)
    gadget = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "shop/gadget_view.html",
        {"gadget": gadget},
    )