from django.shortcuts import render
from main import models
from django.db.models import Q
from main.models import Chairman, MFY, Neighborhood, House, Human
from django.core.paginator import Paginator



def search(request):
    query = request.GET.get('query', '')
    chairman_results = []
    mfy_results = []
    neighborhood_results = []
    house_results = []
    human_results = []

    if query:
        # Har bir model uchun qidiruv
        chairman_results = Chairman.objects.filter(
            Q(name__icontains=query)
        )
        mfy_results = MFY.objects.filter(
            Q(title__icontains=query)
        )
        neighborhood_results = Neighborhood.objects.filter(
            Q(title__icontains=query)
        )
        house_results = House.objects.filter(
            Q(house_number__icontains=query)
        )
        human_results = Human.objects.filter(
            Q(fullname__icontains=query)
        )
    
    return render(request, 'search_results.html', {
        'query': query,
        'chairman_results': chairman_results,
        'mfy_results': mfy_results,
        'neighborhood_results': neighborhood_results,
        'house_results': house_results,
        'human_results': human_results,
    })

# ----------------------------------------------------------------------------------------------------------------------------------------


def ChairmansView(request):
    model = models.Chairman.objects.all()
    filter_information = request.GET.get('information')
    filter_status = request.GET.get('status')
    sort_by = request.GET.get('sort')

    # Filtrlar
    if filter_information and filter_information != '0':
        model = model.filter(information=filter_information)
    if filter_status and filter_status != '0':
        model = model.filter(status=filter_status)
    
    # Saralash
    if sort_by == 'name':
        model = model.order_by('name')
    elif sort_by == 'created':
        model = model.order_by('-created')

    # Pagination
    paginator = Paginator(model, 10)  # Har bir sahifada 10 ta element
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'chairmans.html', context)
# ----------------------------------------------------------------------------------------------------------------------------------------

def MFYView(request):
    model = models.MFY.objects.all()
    sort_by = request.GET.get('sort')

    # Saralash
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

    # Pagination
    paginator = Paginator(model, 10)  # Har bir sahifada 10 ta obyekt
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'chairmans': models.Chairman.objects.all(),
    }
    return render(request, 'MFY.html', context)
# ----------------------------------------------------------------------------------------------------------------------------------------


def NeighborhoodsView(request):
    model = models.Neighborhood.objects.all()
    sort_by = request.GET.get('sort')

    # Saralash
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

    # Pagination
    paginator = Paginator(model, 10)  # Har bir sahifada 10 ta obyekt
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'neighborhoods.html', context)

# ----------------------------------------------------------------------------------------------------------------------------------------


def HousesView(request):
    model = models.House.objects.all()
    filter_status = request.GET.get('status')
    sort_by = request.GET.get('sort')

    # Filtrlar
    if filter_status and filter_status != '0':
        model = model.filter(status=filter_status)
    
    # Saralash
    if sort_by == 'people':
        model = model.order_by('-people')
    elif sort_by == 'area_kv_m':
        model = model.order_by('-area_kv_m')
    elif sort_by == 'created':
        model = model.order_by('-created')

    # Pagination
    paginator = Paginator(model, 10)  # Har bir sahifada 10 ta obyekt
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'houses.html', context)

# ----------------------------------------------------------------------------------------------------------------------------------------




def HumansView(request):
    model = models.Human.objects.all()
    filter_status = request.GET.get('status')
    filter_information = request.GET.get('information')
    filter_house = request.GET.get('house')
    sort_by = request.GET.get('sort')

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

    # Pagination
    paginator = Paginator(model, 10)  # Har bir sahifada 10 ta obyekt
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
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





