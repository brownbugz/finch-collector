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
  path('planners/<int:planner_id>/add_accessory/', views.add_accessory, name='add_accessory'),
  path('planners/<int:planner_id>/assoc_gadget/<int:gadget_id>/', views.assoc_gadget, name='assoc_gadget'),
  path('planners/<int:planner_id>/unassoc_gadget/<int:gadget_id>/', views.unassoc_gadget, name='unassoc_gadget'),
  path('planners/<int:planner_id>/add_photo/', views.add_photo, name='add_photo'),
  path('gadgets/', views.GadgetList.as_view(), name='gadgets_index'),
  path('gadgets/<int:pk>/', views.GadgetDetail.as_view(), name='gadgets_detail'),
  path('gadgets/create/', views.GadgetCreate.as_view(), name='gadgets_create'),
  path('gadgets/<int:pk>/update/', views.GadgetUpdate.as_view(), name='gadgets_update'),
  path('gadgets/<int:pk>/delete/', views.GadgetDelete.as_view(), name='gadgets_delete'),
]