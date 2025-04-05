from .models import Renting, Customer
from django import forms


class DatePickerInput(forms.DateInput):
    input_type = 'date'


class RentingForm(forms.ModelForm):
    class Meta:
        model = Renting
        fields = ('start_date', 'number_days_rent', 'quantity',)
        start_date = forms.DateField(widget=DatePickerInput)

        widgets = {
            'start_date': DatePickerInput(),
        }


class RentEditForm(forms.ModelForm):
    class Meta:
        model = Renting
        fields = ('quantity', 'start_date', 'number_days_rent', 'email', 'phone', 'address',)

        widgets = {
            'start_date': DatePickerInput(),
        }


class RentConfirmForm(forms.ModelForm):
    class Meta:
        model = Renting
        fields = ('status',)


class CustomerProfileRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'age', 'phone', 'email', 'shipping_address',)
