from main import models
from main import serializers 

from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet



class MyPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 100







class  ChairmanViewSet(ModelViewSet):
    queryset = models.Chairman.objects.all()
    serializer_class = serializers.ChairmanSerializer
    pagination_class = MyPagination


# -------------------------------------------------------------------------------------------


class MFYViewSet(ModelViewSet):
    queryset = models.MFY.objects.all()
    serializer_class = serializers.MFYSerializer
    pagination_class = MyPagination

# -------------------------------------------------------------------------------------------


class NeighborhoodViewSet(ModelViewSet):
    queryset = models.Neighborhood.objects.all()
    serializer_class = serializers.NeighborhoodSerializer
    pagination_class = MyPagination
# -------------------------------------------------------------------------------------------


class HouseViewSet(ModelViewSet):
    queryset = models.House.objects.all()
    serializer_class = serializers.HouseSerializer
    pagination_class = MyPagination
# -------------------------------------------------------------------------------------------

class HumanViewSet(ModelViewSet):
    queryset = models.Human.objects.all()
    serializer_class = serializers.HumanSerializer
    pagination_class = MyPagination
    