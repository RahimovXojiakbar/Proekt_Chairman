from django.shortcuts import render
from main import models


def ChairmansView(request):
    model = models.Chairman.objects.all()
    context = {
        'chairmans':model
    }
    return render(request, 'chairmans.html', context)

def MFYView(request):
    model = models.MFY.objects.all()
    context = {
        'MFY':model
    }
    return render(request, 'MFY.html', context)


def NeighborhoodsView(request):
    model = models.Neighborhood.objects.all()
    context = {
        'neighborhoods':model
    }
    return render(request, 'neighborhoods.html', context)



def HousesView(request):
    model = models.House.objects.order_by('-created')[:40]
    context = {
        'houses':model
    }
    return render(request, 'houses.html', context)


def HumansView(request):
    model = models.Human.objects.order_by('-created')[:40]
    context = {
        'humans':model
    }
    return render(request, 'humans.html', context)



# ------------------------------------------------------------------------------------------------------------------------



def ChairmanDetailView(request, id):
    model = models.Chairman.objects.get(id=id)
    context = {
        'chairman_detail':model
    }
    return render(request, 'chairman_detail.html', context)


def MFYDetailView(request, id):
    model = models.MFY.objects.get(id=id)
    context = {
        'MFY_detail':model
    }
    return render(request, 'MFY_detail.html', context)



def NeighborhoodDetailView(request, id):
    model = models.Neighborhood.objects.get(id=id)
    context = {
        'neighborhood_detail':model
    }
    return render(request, 'neighborhood_detail.html', context)




def HouseDetailView(request, id):
    model = models.House.objects.get(id=id)
    context = {
        'house_detail':model
    }
    return render(request, 'house_detail.html', context)




def HumanDetailView(request, id):
    model = models.Human.objects.get(id=id)
    context = {
        'human_detail':model
    }
    return render(request, 'human_detail.html', context)


def index_view(request):
    return render(request, 'index.html', )