from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Gadget, Category, Customer, Renting
from .forms import RentingForm


# Create your views here.
class GadgetList(generic.ListView):
    queryset = Gadget.objects.filter(status=1)
    template_name = "shop/index.html"
    paginate_by = 4


def category(request, dl):
    # Grab the category from the url
    category = Category.objects.get(category_name=dl)
    gadget = Gadget.objects.filter(category=category, status=1)
    return render(request, 'shop/category.html', {'gadget': gadget, 'category': category})


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


def customer_profile(request):
    customer = Customer.objects.get(id=request.user.id)
    print(customer.age)
    return render(request, 'shop/customer_profile.html', {'customer': customer})


def renting_form(request, slug):
    print('about to proceed')
    rentings = Renting.objects.get(id=request.user.id)
    gadget = Gadget.objects.get(slug=slug)
    print(gadget)
    print(rentings)

    if request.method == "POST":
        renting_form = RentingForm(data=request.POST)
        if renting_form.is_valid():
            renting = renting_form.save(commit=False)
            renting.customer = request.user
            renting.gadget = gadget
            renting.save()

    renting_form = RentingForm()

    return render(
        request,
        "shop/renting_form.html",
        {'renting_form': renting_form, 'rentings': rentings, 'gadget': gadget}
    )