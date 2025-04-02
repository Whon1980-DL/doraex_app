from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages
from datetime import date
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
    customer = Customer.objects.get(id=request.user.id+2)
    print(customer)
    print(customer.age)
    return render(request, 'shop/customer_profile.html', {'customer': customer})


def renting_form(request, slug):
    print('about to proceed')
    gadget = Gadget.objects.get(slug=slug)
    print(gadget)
    id = request.user.id+10
    print(id)
    rentings = Renting.objects.get(id=id)
    print(rentings)
    customer = Customer.objects.get(id=request.user.id+2)
    customer_age = customer.age
    usage_age = gadget.minimum_usage_age
    print(customer_age)
    print(usage_age)
    print(customer)
    today_date = date.today()
    print(today_date)

    if request.method == "POST":
        renting_form = RentingForm(data=request.POST)
        if renting_form.is_valid():
            renting = renting_form.save(commit=False)
            renting.customer = request.user
            renting.gadget = gadget
            renting.first_name = customer.first_name
            renting.last_name = customer.last_name
            renting.first_name = customer.shipping_address
            renting.email = customer.email
            renting.phone = customer.phone
            renting.address = customer.shipping_address
            renting.price = gadget.unit_rent_price
            renting.save()

            messages.add_message(request, messages.SUCCESS, "Gadget add to cart please review cart to check out or contitue shopping ")

    renting_form = RentingForm()

    return render(
        request,
        "shop/renting_form.html",
        {'renting_form': renting_form, 'rentings': rentings, 'gadget': gadget, 'customer': customer, 'today_date': today_date},
    )


def cart(request):
    customer = Customer.objects.get(id=request.user.id+2)
    customer_username = customer.customer
    renting_pending = Renting.objects.filter(status=0)
    cart = renting_pending.filter(customer=customer_username)
    gadget_count = cart.all().order_by('-created_on')
    
    return render(
        request, 
        'shop/cart.html', 
        {'cart': cart, 'gadget_count': gadget_count, 'customer': customer},
    )
