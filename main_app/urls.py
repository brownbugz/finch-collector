from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('planners/', views.planners_index, name='index'),
  path('planners/<int:planner_id>', views.planners_detail, name='detail')
]