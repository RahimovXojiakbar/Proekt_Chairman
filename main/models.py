from django.db import models
from django_ckeditor_5.fields import CKEditor5Field





class Chairman(models.Model):
    name = models.CharField(max_length=200)
    BIO = CKEditor5Field(config_name='extends')
    information =  models.CharField(max_length=200, choices={'MIDDLE':'MIDDLE', 'HIGH':'HIGH'})
    status = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class MFY(models.Model):
    title = models.CharField(max_length=200)
    chairman = models.ForeignKey(Chairman, on_delete=models.SET_NULL, null=True)
    area_kv_km = models.DecimalField(decimal_places=2, max_digits=15)
    number_houses = models.PositiveIntegerField()
    people = models.PositiveIntegerField(default=0)
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class Neighborhood(models.Model):   
    title = models.CharField(max_length=200)
    elder = models.CharField(max_length=250)
    MFY = models.ForeignKey(MFY, on_delete=models.SET_NULL, null=True)
    area_kv_km = models.DecimalField(decimal_places=2, max_digits=15)
    number_houses = models.IntegerField()
    people = models.PositiveIntegerField(blank=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class House(models.Model):
    house_boss = models.CharField(max_length=200)
    house_number= models.PositiveIntegerField()
    a_b = models.CharField(max_length=200, choices={ 'A':'A', 'B':'B'})
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, null=True, related_name='house')
    status = models.CharField(max_length=200, choices={'POORER':'POORER', 'MIDDLE':'MIDDLE','RICH':'RICH'})
    people = models.PositiveIntegerField(blank=True)
    area_kv_m = models.DecimalField(decimal_places=2, max_digits=15)
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['house_number', 'a_b']

    def __str__(self) -> str:
        return f"{self.house_number} {self.a_b}"
    

class Human(models.Model):
    fullname = models.CharField(max_length=200)
    BIO = CKEditor5Field(config_name='extends2')
    status = models.CharField(max_length=200, choices={'Kindergarten':'Kindergarten', 'Schoolboy':'Schoolboy', 'Student':'Student', 'Worker':'Worker'})
    information = models.CharField(max_length=200, choices={'NO':'NO', 'MIDDLE':'MIDDLE','HIGH':'HIGH'}, default='NO')
    house = models.ForeignKey(House, on_delete=models.SET_NULL, null=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.fullname




