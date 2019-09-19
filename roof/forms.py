from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['first_name', 'last_name', 'number_phone', 'email', 'date_reservation', 'time_reservation', 'number_persone']
