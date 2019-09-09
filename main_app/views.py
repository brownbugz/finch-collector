from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Planner Collections</h1>')

def about(request):
    return render(request, 'about.html')

def planners_index(request):
    return render(request, 'planners/index.html', { 'planners': planners })

def planners_detail(request, planner_id):
    planner = Planner.objects.get(id=planner_id)
    return render(request, 'planners/detail.html')