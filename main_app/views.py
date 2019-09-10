from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Planner

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
    return render(request, 'planners/detail.html', { 'planner': planner })