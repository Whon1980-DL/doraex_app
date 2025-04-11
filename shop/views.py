from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages
from datetime import date, timedelta
from .models import Gadget, Category, Customer, Renting
from .forms import RentingForm, RentEditForm, CustomerProfileRegistrationForm
from .forms import ProfileEditForm

# Create your views here.


class GadgetList(generic.ListView):
    """
    Returns all published gadgets in :model:`shop.Gadget`
    and displays them in a page of six gadgets.
    **Context**

    ``queryset``
        All published instances of :model:`shop.Gadget`
    ``paginate_by``
        Number of gadgets per page.

    **Template:**

    :template:`shop/index.html`
    """
    queryset = Gadget.objects.filter(status=1)
    template_name = "shop/index.html"
    paginate_by = 6


def contact_view(request):
    """
    Returns contact page.
    **Context**

    :template:`shop/contact.html`
    """
    return render(request, 'shop/contact.html')


def category(request, dl):
    """
    Returns published gadgets in :model:`shop.Gadget`
    related to certain category.

    **Context**

    ``category``
        All instance of :model:`shop.Category`.
    ``gadget``
        All published gadget related to the certain category.

    **Template:**

    :template:`shop/category.html`
    """
    # Grab the category from the url
    category = Category.objects.get(category_name=dl)
    gadget = Gadget.objects.filter(category=category, status=1)
    return render(
        request, 'shop/category.html', 
        {'category': category, 
         'gadget': gadget, }
         )


def gadget_view(request, slug):
    """
    Display an individual :model:`shop.Gadget`.

    **Context**

    ``gadget``
        An instance of :model:`shop.Gadget`.
    ``customer``
        An instance of :model:`shop.Customer`.

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
    """
    Display profile registeration page,
    if user already have a profile a message will display
    telling user they alreay have a profile created. 
    if the method is equal POST, customer enterd detail 
    will be saved to database through form completion.

    **Context**

    ``customer``
        All instances of :model:`shop.Customer``
    ``username``
        An instance of customer related to the user
    ``customer_profile_registration_form``
        An instance of :form:`shop.CustomerProfileRegistrationForm`.
        
    **Template:**

    :template:`blog/customer_profile_registration.html`
    """
    customer = Customer.objects.all()
    username = request.user

    if customer.filter(customer=username).exists():
       
        messages.add_message(
            request, messages.ERROR, 
            "You already have an existing customer profile, "
            "to edit please go to view profile to edit."
                )
        return HttpResponseRedirect(reverse('home', args=[]))

    else:
        if request.method == "POST":
            customer_profile_registration_form = CustomerProfileRegistrationForm(
                data=request.POST
                )
            if customer_profile_registration_form.is_valid():
                customer = customer_profile_registration_form.save(
                    commit=False
                    )
                customer.customer = request.user
                customer_profile_registration_form.save()
                messages.add_message(
                    request, messages.SUCCESS, 
                    "Thank you for creating your customer profile. "
                    "Please head back to our Home to start your renting ")

        customer_profile_registration_form = CustomerProfileRegistrationForm()

        return render(
            request, "shop/customer_profile_registration.html",
            {"customer_profile_registration_form": customer_profile_registration_form},
        )


def customer_profile(request):
    """
    Display customer profile page to allow
    viewing and editing through a form.

    **Context**

    ``customer``
        All instances of :model:`shop.Customer``
    ``username``
        An instance of customer related to the user
    ``profile_edit_form``
        An instance of :form:`shop.ProfileEditForm`.
      
    **Template:**

    :template:`blog/customer_profile.html`
    """
    customer = Customer.objects.all()
    username = request.user

    if customer.filter(customer=username).exists():
        print("Entry contained in queryset")
        customer = Customer.objects.get(customer=request.user)
        profile_edit_form = ProfileEditForm()
        return render(request,
                      'shop/customer_profile.html', 
                      {'customer': customer, 
                       'profile_edit_form': profile_edit_form})
    else:
        messages.add_message(
            request, messages.ERROR, 
            "Please fill in the form below to create your"
            "customer profile and enjoy renting our gadgets!"
            )

        return HttpResponseRedirect(
            reverse('customer_profile_registration', args=[])
            )


def profile_edit_form(request, customer_id):
    """
    Display a customer profile for editing.

    **Context**

    ``customer``
        An customer of :model:`shop.Customer` with specific id.
    ``profile_edit_form``
        An instance of :form:`shop.ProfileEditForm`.
    """
    queryset = Customer.objects.all()
    customer = get_object_or_404(queryset, id=customer_id)
    profile_edit_form = ProfileEditForm(data=request.POST, instance=customer)

    if request.method == "POST":
        if profile_edit_form.is_valid():
            profile = profile_edit_form.save(commit=False)
            profile.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Profile Updated!'
                )
        else:
            messages.add_message(
                request, messages.ERROR,
                'Error updating Profile!'
                )

    return HttpResponseRedirect(reverse('customer_profile', args=[]))


def renting_form(request, slug):
    """
    Display renting form and save entered detail
    to create new instance of :model:`shop.Rent`.
    if usre does not already have a customer profile
    they wil be reuired to create by directing them to
    customer profile registration page.

    **Context**

    ``gadget``
        An instance of :model:`shop.Gadget`
        with specific slug.
    ``today_date``
        A value of today date.
    ``customer``
        All instance of :model:`shop.Customer`.
    ``renting_form``
        An instance of :form:`shop.RentingForm`

    **Template:**

    :template:`shop/renting_form.html`
    """
    gadget = Gadget.objects.get(slug=slug)
    today_date = date.today()
    customer = Customer.objects.all()
    username = request.user

    if customer.filter(customer=username).exists():
        customer = Customer.objects.get(customer=request.user)
        if request.method == "GET":

            renting_form = RentingForm()
            return render(request,
                          "shop/renting_form.html",
                          {'renting_form': renting_form,
                           'gadget': gadget, 
                           'customer': customer,
                           'today_date': today_date},
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
                end_date = renting.start_date + timedelta(
                    days=renting.number_days_rent
                    )
                renting.end_date = end_date
                renting.save()

                messages.add_message(
                    request, messages.SUCCESS, 
                    "Gadget added please review 'My Rented Gadget"
                    "to confirm you rent and checkout or contitue shopping "
                    )

        return HttpResponseRedirect(reverse('cart', args=[]))
    else:
        if request.method == "GET":
            customer_profile_registration_form = CustomerProfileRegistrationForm()
            messages.add_message(
                request, messages.ERROR,
                'Please fill in the form below to create your '
                'customer profile before you can rent our gadgets'
                )

            return render(request,
                          "shop/customer_profile_registration.html",
                          {'customer_profile_registration_form':
                           customer_profile_registration_form},
                          )
        if request.method == "POST":
            customer_profile_registration_form = CustomerProfileRegistrationForm(
                data=request.POST
                )
            if customer_profile_registration_form.is_valid():
                
                customer = customer_profile_registration_form.save(
                    commit=False
                    )
                customer.customer = request.user
                customer_profile_registration_form.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    "Thank you for creating your customer profile. "
                    "Please continue to enjoy your renting experience"
                    )
                

                customer_profile_registration_form = CustomerProfileRegistrationForm()

                renting_form = RentingForm()
                return render(request,
                              "shop/renting_form.html",
                              {'renting_form': renting_form,
                               'gadget': gadget,
                               'customer': customer,
                               'today_date': today_date},
                              )


def cart(request):
    """
    Display a list of rented gadget to allow deleting,
    editing and confirming.

    **Context**

    ``customer``
        An instance of :model:`blog.Customer` related user.
    ``renting``
        All instance of :model:`shop.Renting`.
    ``customer_rent``
        All instance of :model:`shop.Renting` related to the customer.
    ``cart_list``
        An instance of :model:`shop.Renting` related to customer
        that is still have status equal pending.
    ``gadget_count_overall``
        A number of customer_rent in total
    ``gadget_count_pending``
        A number of customer_rent that is still pending
    ``rent_edit_form``
        An instance of :form:`shop.RentEditForm`

    **Template:**

    :template:`shop/cart.html`
    """
    customer = request.user
    renting = Renting.objects.all()
    customer_rent = renting.filter(customer=customer)
    cart_list = customer_rent.all().order_by('status', '-created_on')
    gadget_count_overall = cart_list.all().count
    gadget_count_pending = cart_list.filter(status=0).count()
    rent_edit_form = RentEditForm()
    
    return render(request, 'shop/cart.html', 
                  {'cart_list': cart_list, 
                   'gadget_count_pending': gadget_count_pending,
                      'customer': customer, 
                      'rent_edit_form': rent_edit_form, 
                      'gadget_count_overall': gadget_count_overall},
                  )


def renting_edit_form(request, renting_id):
    """
   Edit an individual renting.

    **Context**

    ``renting``
        An instance of :model:`shop.Renting` related to specific renting id.
    ``rent_edit_form``
        An instance of :form:`shop.RentEditForm`
    """
    
    if request.method == "POST":
        
        queryset = Renting.objects.filter(status=0)
        renting = get_object_or_404(queryset, pk=renting_id)
        rent_edit_form = RentEditForm(data=request.POST, instance=renting)
        
        if rent_edit_form.is_valid():
            renting = rent_edit_form.save(commit=False)
            end_date = renting.start_date + timedelta(
                days=renting.number_days_rent
                )
            renting.end_date = end_date
            renting.save()
            messages.add_message(
                request, messages.SUCCESS, 
                'Renting Updated!'
                )
        else:
            messages.add_message(
                request, messages.ERROR, 
                'Error updating Renting!'
                )

    return HttpResponseRedirect(reverse('cart', args=[]))


def renting_confirm(request, renting_id):
    """
    Confirm an individual renting.

    **Context**

    ``queryset``
        A set of instance of :model:`shop.Renting` 
        with a status of pedning.
    ``renting``
        An instance of :model:`shop.Renting`
        related to certain primary key
    """

    queryset = Renting.objects.filter(status=0)
    renting = get_object_or_404(queryset, pk=renting_id)
    renting.status = 1
    renting.save()
    messages.add_message(
            request, messages.SUCCESS, 
            "Your rent is confirmed and your gadget are on their way. "
            "Please pay upon delivery"
            )
    return HttpResponseRedirect(reverse('cart', args=[]))


def renting_delete(request, renting_id):
    """
    Delete an individual renting

    **Context**

    ``queryset``
        A set of instance of :model:`shop.Renting`
        with a status of pedning.
    ``renting``
        An instance of :model:`shop.Renting`
        related to certain primary key
    """
    queryset = Renting.objects.filter(status=0)
    renting = get_object_or_404(queryset, pk=renting_id)
    renting.delete()
    messages.add_message(request, messages.SUCCESS, 'Renting deleted!')

    return HttpResponseRedirect(reverse('cart', args=[]))
