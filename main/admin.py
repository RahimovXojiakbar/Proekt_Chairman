from django.contrib import admin
from unfold.admin import ModelAdmin
from main import models




@admin.register(models.Chairman)
class ChairmanAdmin(ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['information', 'status']



@admin.register(models.MFY)
class MFYAdmin(ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']
    list_filter = ['chairman']



@admin.register(models.Neighborhood)
class NeighborhoodAdmin(ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']
    list_filter = ['MFY']




@admin.register(models.House)
class HouseAdmin(ModelAdmin):
    list_display = ['id', 'house_number']
    search_fields = ['house_number']
    list_filter = ['a_b', 'neighborhood', 'status']



@admin.register(models.Human)
class HumanAdmin(ModelAdmin):
    list_display = ['id', 'fullname']
    search_fields = ['fullname']
    list_filter = ['status', 'information', 'house__status']

    
