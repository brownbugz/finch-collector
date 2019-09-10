from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Planner
from .forms import AccessoryForm

class PlannerCreate(CreateView):
    model = Planner
    fields = '__all__'
    success_url = '/planners/'

class PlannerUpdate(UpdateView):
  model = Planner
  fields = ['brand', 'description', 'year']

class PlannerDelete(DeleteView):
  model = Planner
  success_url = '/planners/'

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def planners_index(request):
    planners = Planner.objects.all()
    return render(request, 'planners/index.html', { 'planners': planners })

def planners_detail(request, planner_id):
    planner = Planner.objects.get(id=planner_id)
    accessory_form = AccessoryForm()
    return render(request, 'planners/detail.html', 
      { 'planner': planner, 'accessory_form': accessory_form })

def add_accessory(request, planner_id):
  form = AccessoryForm(request.POST)
  if form.is_valid():
    new_accessory = form.save(commit=False)
    new_accessory.planner_id = planner_id
    new_accessory.save()
  return redirect('detail', planner_id=planner_id)