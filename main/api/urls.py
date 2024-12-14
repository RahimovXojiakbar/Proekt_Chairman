from django.urls import path
from . import views

urlpatterns = [
  path('chairmans/', views.ChairmanListView.as_view(), name='chairman_list_url'),
  path('MFY/', views.MFYListView.as_view(), name='MFY_list_url'),
  path('neighborhoods/', views.NeighborhoodListView.as_view(), name='neighborhood_list_url'),
  path('houses/', views.HouseListView.as_view(), name='house_list_url'),
  path('humans/', views.HumanListView.as_view(), name='human_list_url'),

  path('chairman/<int:pk>/', views.ChairmanDetailView.as_view(), name='chairman_detail_url'),
  path('MFY/<int:pk>/', views.MFYDetailView.as_view(), name='MFY_detail_url'),
  path('neighborhood/<int:pk>/', views.NeighborhoodDetailView.as_view(), name='neighborhood_detail_url'),
  path('house/<int:pk>/', views.HouseDetailView.as_view(), name='house_detail_url'),
  path('human/<int:pk>/', views.HumanDetailView.as_view(), name='human_detail_url'),

]   
