from django.urls import path
from main.dashboard import views

urlpatterns = [
    path('chairmans/', views.ChairmansView, name='chairmans_url'),
    path('MFY/', views.MFYView, name='MFY_url'),
    path('neighborhoods/', views.NeighborhoodsView, name='neighborhoods_url'),
    path('houses/', views.HousesView, name='houses_url'),
    path('humans/', views.HumansView, name='humans_url'),
    
    path('chairman_detail/<int:id>/', views.ChairmanDetailView, name='chairman_detail_url'),
    path('MFY_detail/<int:id>/', views.MFYDetailView, name='MFY_detail_url'),
    path('neighborhood_detail/<int:id>/', views.NeighborhoodDetailView, name='neighborhood_detail_url'),
    path('house_detail/<int:id>/', views.HouseDetailView, name='house_detail_url'),
    path('human_detail/<int:id>/', views.HumanDetailView, name='human_detail_url'),
]   