from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Rescue
from .forms import GiftForm
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
    gift_form = GiftForm()
    return render(request, 'rescues/detail.html', {'rescue': rescue, 'gift_form': gift_form})

class RescueCreate(CreateView):
    model = Rescue
    fields = '__all__'

class RescueUpdate(UpdateView):
    model = Rescue
    fields = ['animal', 'description', 'age']

class RescueDelete(DeleteView):
    model = Rescue
    success_url = '/rescues/'


def add_gift(request, rescue_id):
  form = GiftForm(request.POST)
  if form.is_valid():
    new_gift = form.save(commit=False)
    new_gift.rescue_id = rescue_id
    new_gift.save()
  return redirect('detail', rescue_id=rescue_id)