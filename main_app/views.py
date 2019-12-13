from django.shortcuts import render
from django.http import HttpResponse
from .models import Rescue
# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def rescues_index(request):
    rescues = Rescue.objects.all()
    return render(request, 'rescues/index.html', {'rescues': rescues})

def rescues_detail(request, rescue_id):
    rescue = Rescue.objects.get(id=rescue_id)
    return render(request, 'rescues/detail.html', {'rescue': rescue})