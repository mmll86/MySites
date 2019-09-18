from django.shortcuts import render
from .models import *
from django.db.models import Q

# Create your views here.
def index(request):
	kitchen_hot = MenuKitchenHot.objects.all()
	context = {'kitchen_hot': kitchen_hot}
	return render(request, 'roof/index.html', context)

def reservation(request):
	reservation = Reservation.objects.all()
	reservation.

		(first_name = request.POST['first_name'], last_name = request.POST['last_name'], number_phone = request.POST['number_phone'], email = request.POST['email'], date_reservation = request.POST['date_reservation'], time_reservation = request.POST['time_reservation'], number_persone = request.POST['number_persone'])
	return render(request, 'roof/reservation.html')