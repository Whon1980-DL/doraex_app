from .models import Renting
from django import forms


class RentingForm(forms.ModelForm):
    class Meta:
        model = Renting
        fields = ('first_name', 'last_name', 'start_date', 'end_date', 'address', 'phone',)

