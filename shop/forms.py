from .models import Renting
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

        