import os
import random
import django
from string import ascii_letters, digits
from random import choices, choice


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from faker import Faker
from main import models




models.Chairman.objects.all().delete()
models.MFY.objects.all().delete()
models.Neighborhood.objects.all().delete()
models.House.objects.all().delete()
models.Human.objects.all().delete()


fake = Faker()




for _ in range(10):
    chairman = models.Chairman.objects.create(
        name = fake.name_male(),
        BIO = fake.text(),
        information = fake.random_element(['MIDDLE', 'HIGH']),
        status = fake.random_element(['True', 'False']),    
    )
    chairman.save()
models.Chairman.objects.all()
print('Add Chairmans')


# =======================================================================================================



for _ in range(15):
    MFY = models.MFY.objects.create(
        title = fake.word().capitalize(),
        chairman = choice(models.Chairman.objects.all()),
        area_kv_km = round(random.uniform(8, 14), 2),
        number_houses = round(random.uniform(250, 350)),
        people = round(random.uniform(900, 1400)),
    )
    MFY.save()
models.MFY.objects.all()
print("Add MFY")


# =======================================================================================================


for _ in range(45):
    neighborhoods = models.Neighborhood.objects.create(
        title = fake.word().capitalize(),
        elder = fake.name_male(),
        MFY = choice(models.MFY.objects.all()),
        area_kv_km = round(random.uniform(2, 9), 2),
        number_houses = round(random.uniform(70, 120)),
        people = round(random.uniform(360, 500)),

    )
    neighborhoods.save()
models.Neighborhood.objects.all()
print('Add Neighborhoods')


# =======================================================================================================


for _ in range(300):
    houses = models.House.objects.create(
        house_boss = fake.name_male(),
        house_number = round(random.uniform(1, 99)),
        a_b = choice(['A', "B"]),
        status = fake.random_element(['POORER', 'MIDDLE', 'RICH']),
        neighborhood = choice(models.Neighborhood.objects.all()),
        area_kv_m = round(random.uniform(200, 1900), 2),
        people = round(random.uniform(1, 12)),

    )
    houses.save()
models.House.objects.all()
print('Add Houses')


# =======================================================================================================


for _ in range(1550):
    
    status = fake.random_element(['Kindergarten', 'Schoolboy', 'Student', 'Worker'])
    
    if status in ['Kindergarten', 'Schoolboy', 'Student']:
        information = 'NO'
    else:
        information = fake.random_element(['NO', 'MIDDLE', 'HIGH'])

    humans = models.Human.objects.create(
        fullname = fake.name(),
        BIO = fake.text(),
        status=status,
        information=information,
        house = choice(models.House.objects.all()),
            

    )
    humans.save()
models.Human.objects.all()
print('Add Humans')



