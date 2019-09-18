from django import forms

class ReservationForm(forms.Form):
    first_name = forms.CharField('Имя', max_length=20)
    last_name = forms.CharField('Фамилия', max_length=20)
    number_phone = forms.CharField('Номер телефона', max_length=12)
    email = forms.CharField('E-email', max_length=20)
    date_reservation = forms.DateField('Дата бронирования')
    time_reservation = forms.TimeField('Время бронирования')
    number_persone = forms.IntegerField('Количество персон')
