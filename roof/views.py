from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from .forms import ReservationForm
from django.views.generic import View


# Create your views here.
def index(request):
	kitchen_hot = MenuKitchenHot.objects.all()
	context = {'kitchen_hot': kitchen_hot}
	return render(request, 'roof/index.html', context)


class ReservationCreate(View):
	def get(self, request):
		form = ReservationForm()
		return render(request, 'roof/reservation.html', context={'form': form})

	def post(self, request):
		bound_form = ReservationForm(request.POST)

		if bound_form.is_valid():
			new_reservation = bound_form.save()

			return redirect(new_reservation)

		return render(request, 'roof/reservation.html', context={'form': bound_form})

