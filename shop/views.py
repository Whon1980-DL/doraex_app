from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages
from datetime import date, timedelta
from django.http import HttpResponseRedirect
from .models import Gadget, Category, Customer, Renting
from .forms import RentingForm, RentEditForm, RentConfirmForm, CustomerProfileRegistrationForm


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
    print(request.user.id)
    gadget = Gadget.objects.get(slug=slug)
    customer = Customer.objects.get(id=request.user.id+2)
    today_date = date.today()

    if request.method == "POST":
        renting_form = RentingForm(data=request.POST)
        if renting_form.is_valid():
            renting = renting_form.save(commit=False)
            renting.customer = request.user
            renting.gadget = gadget
            renting.first_name = customer.first_name
            renting.last_name = customer.last_name
            renting.email = customer.email
            renting.phone = customer.phone
            renting.address = customer.shipping_address
            renting.price = gadget.unit_rent_price
            end_date = renting.start_date + timedelta(days=renting.number_days_rent)
            renting.end_date = end_date
            renting.save()

            messages.add_message(request, messages.SUCCESS, "Gadget add to cart please review cart to check out or contitue shopping ")

    renting_form = RentingForm()

    return render(
        request,
        "shop/renting_form.html",
        {'renting_form': renting_form, 'gadget': gadget, 'customer': customer, 'today_date': today_date},
    )


def cart(request):
    customer = Customer.objects.get(id=request.user.id+2)
    customer_username = customer.customer
    renting_pending = Renting.objects.filter(status=0)
    cart = renting_pending.filter(customer=customer_username)
    cart_list = cart.all().order_by('-created_on')
    gadget_count = cart.all().count()
    print('about to count')
    print(gadget_count)
    rent_edit_form = RentEditForm()
    print(request)
    
    return render(
        request, 
        'shop/cart.html',
        {'cart_list': cart_list, 'gadget_count': gadget_count, 'customer': customer, 'rent_edit_form': rent_edit_form},
    )


def renting_edit_form(request, renting_id):

    if request.method == "POST":
        
        queryset = Renting.objects.filter(status=0)
        renting = get_object_or_404(queryset, pk=renting_id)
        rent_edit_form = RentEditForm(data=request.POST, instance=renting)
        
        if rent_edit_form.is_valid():
            renting = rent_edit_form.save(commit=False)
            end_date = renting.start_date + timedelta(days=renting.number_days_rent)
            renting.end_date = end_date
            renting.save()
            messages.add_message(request, messages.SUCCESS, 'Renting Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating Renting!')

    return HttpResponseRedirect(reverse('cart', args=[]))


def renting_confirm(request, renting_id):

    queryset = Renting.objects.filter(status=0)
    renting = get_object_or_404(queryset, pk=renting_id)
    renting.status = 1
    renting.save()
    messages.add_message(
        request, messages.SUCCESS, 
        'Your rent is confirmed and your gadget are on their way. Please pay upon delivery'
        )
    
    return HttpResponseRedirect(reverse('cart', args=[]))


def renting_delete(request, renting_id):
    """
    view to delete renting
    """
    queryset = Renting.objects.filter(status=0)
    renting = get_object_or_404(queryset, pk=renting_id)
    renting.delete()
    messages.add_message(request, messages.SUCCESS, 'Renting deleted!')

    return HttpResponseRedirect(reverse('cart', args=[]))


def customer_profile_registration(request):

    username = request.user

    if request.method == "POST":
        customer_profile_registration_form = CustomerProfileRegistrationForm(data=request.POST)
        if customer_profile_registration_form.is_valid():
            customer = customer_profile_registration_form.save(commit=False)
            customer.customer = username
            customer_profile_registration_form.save()
            messages.add_message(request, messages.SUCCESS, "Thank you ")

    customer_profile_registration_form = CustomerProfileRegistrationForm()

    return render(
        request, "shop/customer_profile_registration.html",
        {"customer_profile_registration_form": customer_profile_registration_form},
    )