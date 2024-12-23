from django.shortcuts import render
from main import models



def ChairmansView(request):
    model = models.Chairman.objects.all()
    filter_information = request.GET.get('information')
    filter_status = request.GET.get('status')
    sort_by = request.GET.get('sort')


    if filter_information and filter_information != '0':
            model = model.filter(information = filter_information)
    if filter_status and filter_status != '0':
            model = model.filter(status = filter_status)
    if sort_by == 'name':
        model = model.order_by('name')
    elif sort_by == 'created':
        model = model.order_by('-created')


    context = {
        'chairmans':model,
        
    }
    return render(request, 'chairmans.html', context)

# ----------------------------------------------------------------------------------------------------------------------------------------

def MFYView(request):
    model = models.MFY.objects.all()
    sort_by = request.GET.get('sort')



    if sort_by == 'title':
        model = model.order_by('title')
    elif sort_by == 'area_kv_km':
        model = model.order_by('-area_kv_km')
    elif sort_by == 'number_houses':
        model = model.order_by('-number_houses')
    elif sort_by == 'people':
        model = model.order_by('-people')
    elif sort_by == 'created':
        model = model.order_by('-created')

    context = {
        'MFY':model,
        'chairmans':models.Chairman.objects.all()
    }
    return render(request, 'MFY.html', context)

# ----------------------------------------------------------------------------------------------------------------------------------------


def NeighborhoodsView(request):
    model = models.Neighborhood.objects.all()
    sort_by = request.GET.get('sort')

    if sort_by == 'title':
        model = model.order_by('title')
    elif sort_by == 'area_kv_km':
        model = model.order_by('-area_kv_km')
    elif sort_by == 'number_houses':
        model = model.order_by('-number_houses')
    elif sort_by == 'people':
        model = model.order_by('-people')
    elif sort_by == 'created':
        model = model.order_by('-created')

    context = {
        'neighborhoods':model
    }
    return render(request, 'neighborhoods.html', context)

# ----------------------------------------------------------------------------------------------------------------------------------------


def HousesView(request):
    model = models.House.objects.all()
    filter_status = request.GET.get('status')
    sort_by = request.GET.get('sort')


    if filter_status and filter_status != '0':
        model = model.filter(status = filter_status)
    
    if sort_by == 'people':
        model = model.order_by('-people')
    elif sort_by == 'area_kv_m':
        model = model.order_by('-area_kv_m')
    elif sort_by == 'created':
        model = model.order_by('-created')

    

    context = {
        'houses':model
    }
    return render(request, 'houses.html', context)

# ----------------------------------------------------------------------------------------------------------------------------------------


def HumansView(request):
    model = models.Human.objects.all()
    filter_status = request.GET.get('status')
    filter_information = request.GET.get('information')
    filter_house = request.GET.get('house')
    sort_by = request.GET.get('sort_by')


    if filter_status and filter_status != '0':
        model = model.filter(status=filter_status)

    if filter_information and filter_information != '0':
        model = model.filter(information=filter_information)

    if filter_house and filter_house != '0':
        model = model.filter(house__id=filter_house)

    if sort_by == 'fullname':
        model = model.order_by('fullname')
    elif sort_by == 'created':
        model = model.order_by('created')

    context = {
        'humans': model,
        'houses': models.House.objects.all(),
    }
    return render(request, 'humans.html', context)



# ------------------------------------------------------------------------------------------------------------------------



def ChairmanDetailView(request, id):
    model = models.Chairman.objects.get(id=id)
    context = {
        'chairman_detail':model
    }
    return render(request, 'chairman_detail.html', context)

# ------------------------------------------------------------------------------------------------------------------------


def MFYDetailView(request, id):
    model = models.MFY.objects.get(id=id)
    context = {
        'MFY_detail':model
    }
    return render(request, 'MFY_detail.html', context)

# ------------------------------------------------------------------------------------------------------------------------


def NeighborhoodDetailView(request, id):
    model = models.Neighborhood.objects.get(id=id)
    context = {
        'neighborhood_detail':model
    }
    return render(request, 'neighborhood_detail.html', context)

# ------------------------------------------------------------------------------------------------------------------------



def HouseDetailView(request, id):
    model = models.House.objects.get(id=id)
    context = {
        'house_detail':model
    }
    return render(request, 'house_detail.html', context)

# ------------------------------------------------------------------------------------------------------------------------



def HumanDetailView(request, id):
    model = models.Human.objects.get(id=id)
    context = {
        'human_detail':model,
    }
    return render(request, 'human_detail.html', context)

# ------------------------------------------------------------------------------------------------------------------------





