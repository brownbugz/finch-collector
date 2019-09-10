from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('planners/', views.planners_index, name='index'),
  path('planners/<int:planner_id>/', views.planners_detail, name='detail'),
  path('planners/create/', views.PlannerCreate.as_view(), name='planners_create'),
  path('planners/<int:pk>/update/', views.PlannerUpdate.as_view(), name='planners_update'),
  path('planners/<int:pk>/delete/', views.PlannerDelete.as_view(), name='planners_delete'),
  path('cats/<int:planner_id>/add_accessory/', views.add_accessory, name='add_accessory'),
]