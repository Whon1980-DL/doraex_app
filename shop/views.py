from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages
from datetime import date, timedelta
from .models import Gadget, Category, Customer, Renting
from .forms import RentingForm, RentEditForm, CustomerProfileRegistrationForm, ProfileEditForm


# Create your views here.
class GadgetList(generic.ListView):
    queryset = Gadget.objects.filter(status=1)
    template_name = "shop/index.html"
    paginate_by = 4


def home_view(request):
    return render(request, 'shop/home.html')


def contact_view(request):
    return render(request, 'shop/contact.html')


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
    customer = request.user

    return render(
        request,
        "shop/gadget_view.html",
        {"gadget": gadget, "customer": customer},
    )


def customer_profile_registration(request):

    customer = Customer.objects.all()
    username = request.user

    if customer.filter(customer=username).exists(): 
        messages.add_message(request, messages.ERROR, "You already haver an existing customer profile to edit please go to view profile to edit")
        print('line 57')
        return HttpResponseRedirect(reverse('home', args=[]))

    else:
        print('line 61')
        if request.method == "POST":
            customer_profile_registration_form = CustomerProfileRegistrationForm(data=request.POST)
            print('line 64')
            if customer_profile_registration_form.is_valid():
                print('line 66')
                customer = customer_profile_registration_form.save(commit=False)
                customer.customer = request.user
                customer_profile_registration_form.save()
                messages.add_message(request, messages.SUCCESS, "Thank you for creating your customer profile. Please head back to our Home to start your renting ")
                print('line 70')
        customer_profile_registration_form = CustomerProfileRegistrationForm()

        return render(
            request, "shop/customer_profile_registration.html",
            {"customer_profile_registration_form": customer_profile_registration_form},
            print('line 76')
        )


def customer_profile(request):

    customer = Customer.objects.all()
    username = request.user

    if customer.filter(customer=username).exists(): 
        print("Entry contained in queryset")
        customer = Customer.objects.get(customer=request.user)
        profile_edit_form = ProfileEditForm()
        return render(request, 'shop/customer_profile.html', {'customer': customer, 'profile_edit_form': profile_edit_form})
    else:
        messages.add_message(request, messages.ERROR, 'Please fill in the form below to create your customer profile and enjoy renting our gadgets!')

        return HttpResponseRedirect(reverse('customer_profile_registration', args=[]))


def profile_edit_form(request, customer_id):

    queryset = Customer.objects.all()
    customer = get_object_or_404(queryset, id=customer_id)
    profile_edit_form = ProfileEditForm(data=request.POST, instance=customer)

    if request.method == "POST":
        if profile_edit_form.is_valid():
            profile = profile_edit_form.save(commit=False)
            profile.save()
            messages.add_message(request, messages.SUCCESS, 'Profile Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating Profile!')

    return HttpResponseRedirect(reverse('customer_profile', args=[]))


def renting_form(request, slug):
    print(request.user.id)
    gadget = Gadget.objects.get(slug=slug)
    today_date = date.today()
    customer = Customer.objects.all()
    username = request.user

    if customer.filter(customer=username).exists(): 
        customer = Customer.objects.get(customer=request.user)
        print(request.method)
        if request.method == "GET":

            renting_form = RentingForm()
            return render(request, 
                          "shop/renting_form.html", 
                          {'renting_form': renting_form, 'gadget': gadget, 'customer': customer, 'today_date': today_date},
                          )
        
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

        return HttpResponseRedirect(reverse('cart', args=[]))
    
    else:
        if request.method == "GET":

            customer_profile_registration_form = CustomerProfileRegistrationForm()

            messages.add_message(request, messages.ERROR, 'Please fill in the form below to create your customer profile before you can rent our gadgets')

            return render(request, 
                          "shop/customer_profile_registration.html", 
                          {'customer_profile_registration_form': customer_profile_registration_form},
                          )
        if request.method == "POST":
            customer_profile_registration_form = CustomerProfileRegistrationForm(data=request.POST)
            print('line 64')
            if customer_profile_registration_form.is_valid():
                print('line 66')
                customer = customer_profile_registration_form.save(commit=False)
                customer.customer = request.user
                customer_profile_registration_form.save()
                messages.add_message(request, messages.SUCCESS, "Thank you for creating your customer profile. Please continue to enjoy your renting experience")
                print('line 70')

                customer_profile_registration_form = CustomerProfileRegistrationForm()

                renting_form = RentingForm()
                return render(request, "shop/renting_form.html", 
                              {'renting_form': renting_form, 'gadget': gadget, 'customer': customer, 'today_date': today_date},
                              )


def cart(request):
    print('about to render cart')
    customer = request.user
    renting = Renting.objects.all()
    customer_rent = renting.filter(customer=customer)
    cart_list = customer_rent.all().order_by('status', '-created_on')
    print(cart_list)
    gadget_count = cart_list.filter(status=0).count()
    rent_edit_form = RentEditForm()
    
    return render(request, 'shop/cart.html', 
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




