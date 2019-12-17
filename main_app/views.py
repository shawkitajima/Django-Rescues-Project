from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Rescue, Adopter, Photo
from .forms import GiftForm
import uuid
import boto3

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
    adopters_rescue_doesnt_have = Adopter.objects.exclude(id__in = rescue.adopters.all().values_list('id'))
    gift_form = GiftForm()
    return render(request, 'rescues/detail.html', {'rescue': rescue, 'gift_form': gift_form, 'adopters': adopters_rescue_doesnt_have})

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

def assoc_adopter(request, rescue_id, adopter_id):
    Rescue.objects.get(id=rescue_id).adopters.add(adopter_id)
    return redirect('detail', rescue_id=rescue_id)

def disassoc_adopter(request, rescue_id, adopter_id):
    Rescue.objects.get(id=rescue_id).adopters.remove(adopter_id)
    return redirect('detail', rescue_id=rescue_id)

class AdopterList(ListView):
    model = Adopter

class AdopterDetail(DetailView):
    model = Adopter

class AdopterUpdate(UpdateView):
    model = Adopter
    fields = ['description']

class AdopterDelete(DeleteView):
    model = Adopter
    success_url = '/adopters/'

class AdopterCreate(CreateView):
    model = Adopter
    fields = '__all__'


def add_photo(request, rescue_id):
    S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
    BUCKET = 'catcollectorshawkitajima'
    rescue_photo = request.FILES.get('photo-file', None)
    if rescue_photo:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:7] + rescue_photo.name[rescue_photo.name.rfind('.'):]
        try:
            s3.upload_fileobj(rescue_photo, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, rescue_id = rescue_id)
            photo.save()
        except:
            print ('lol you done messed up')
    return redirect('detail', rescue_id=rescue_id)