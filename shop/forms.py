from django import forms
from .models import Renting, Customer


class DatePickerInput(forms.DateInput):
    """
    Date input class to allow date picking function
    """
    input_type = 'date'


class CustomerProfileRegistrationForm(forms.ModelForm):
    """
    Form class for users to create their customer profile
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = Customer
        fields = (
            'first_name',
            'last_name',
            'age', 'phone',
            'email', 'shipping_address',
            )


class ProfileEditForm(forms.ModelForm):
    """
    Form class for users to edit their customer profile
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = Customer
        fields = ('first_name', 'last_name', 'age',
                  'phone', 'email', 'shipping_address',
                  )


class RentingForm(forms.ModelForm):
    """
    Form class for users to provide rental detail
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = Renting
        fields = ('start_date', 'number_days_rent', 'quantity',)
        start_date = forms.DateField(widget=DatePickerInput)

        widgets = {
            'start_date': DatePickerInput(),
        }


class RentEditForm(forms.ModelForm):
    """
    Form class for users to edit their renting detail
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = Renting
        fields = ('quantity', 'start_date', 'number_days_rent',
                  'email', 'phone', 'address',
                  )

        widgets = {
            'start_date': DatePickerInput(),
        }
