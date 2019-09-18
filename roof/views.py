from django.shortcuts import render
from .models import *
from django.db.models import Q

# Create your views here.
def index(request):
	kitchen_hot = MenuKitchenHot.objects.all()
	context = {'kitchen_hot': kitchen_hot}
	return render(request, 'roof/index.html', context)

