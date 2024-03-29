from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
from .models import Planner, Gadget, Photo
from .forms import AccessoryForm

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'catcollector-sjk'

class PlannerCreate(CreateView):
  model = Planner
  fields = ['name', 'brand', 'description', 'year']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


class PlannerUpdate(UpdateView):
  model = Planner
  fields = ['brand', 'description', 'year']

class PlannerDelete(DeleteView):
  model = Planner
  success_url = '/planners/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def planners_index(request):
    planners = Planner.objects.all()
    return render(request, 'planners/index.html', { 'planners': planners })

@login_required
def planners_detail(request, planner_id):
    planner = Planner.objects.get(id=planner_id)
    gadgets_planner_doesnt_have = Gadget.objects.exclude(id__in = planner.gadgets.all().values_list('id'))
    accessory_form = AccessoryForm()
    return render(request, 'planners/detail.html', { 
        'planner': planner, 'accessory_form': accessory_form,
        'gadgets': gadgets_planner_doesnt_have
    })

@login_required
def add_accessory(request, planner_id):
  form = AccessoryForm(request.POST)
  if form.is_valid():
    new_accessory = form.save(commit=False)
    new_accessory.planner_id = planner_id
    new_accessory.save()
  return redirect('detail', planner_id=planner_id)

@login_required
def add_photo(request, planner_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, planner_id=planner_id)
      photo.save()
    except:
      print('An error occurred uploading file to S3')
  return redirect('detail', planner_id=planner_id)

@login_required
def assoc_gadget(request, planner_id, gadget_id):
  Planner.objects.get(id=planner_id).gadgets.add(gadget_id)
  return redirect('detail', planner_id=planner_id)

@login_required
def unassoc_gadget(request, planner_id, gadget_id):
  Planner.objects.get(id=planner_id).gadgets.remove(gadget_id)
  return redirect('detail', planner_id=planner_id)

class GadgetList(ListView):
  model = Gadget

class GadgetDetail(DetailView):
  model = Gadget

class GadgetCreate(CreateView):
  model = Gadget
  fields = '__all__'

class GadgetUpdate(UpdateView):
  model = Gadget
  fields = ['name', 'color']

class GadgetDelete(DeleteView):
  model = Gadget
  success_url = '/gadgets/'


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {
    'form': form,
    'error_message': error_message
  }
  return render(request, 'registration/signup.html', context)