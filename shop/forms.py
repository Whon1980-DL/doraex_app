from .models import Renting
from django import forms


class DatePickerInput(forms.DateInput):
    input_type = 'date'


class RentingForm(forms.ModelForm):
    class Meta:
        model = Renting
        fields = ('start_date', 'end_date', 'number_days_rent', 'quantity',)
        start_date = forms.DateField(widget=DatePickerInput)
        end_date = forms.DateField(widget=DatePickerInput)

        widgets = {
            'start_date': DatePickerInput(),
            'end_date': DatePickerInput(),
        }

