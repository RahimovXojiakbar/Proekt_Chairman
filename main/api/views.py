from django.shortcuts import render
from main import models
from main import serializers 
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from django_filters.rest_framework import  DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination

class MyPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class ChairmanListView(ListAPIView):
    queryset = models.Chairman.objects.all()
    serializer_class = serializers.ChairmanListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['information', 'status']
    search_fields = ['name']
    pagination_class  = MyPagination


class MFYListView(ListAPIView):
    queryset = models.MFY.objects.all()
    serializer_class = serializers.MFYListSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title']
    pagination_class  = MyPagination


class NeighborhoodListView(ListAPIView):
    queryset = models.Neighborhood.objects.all()
    serializer_class = serializers.NeighborhoodListSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title']
    pagination_class  = MyPagination


class HouseListView(ListAPIView):
    queryset = models.House.objects.all()
    serializer_class = serializers.HouseListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['neighborhood', 'a_b']
    search_fields = ['house_number']
    pagination_class  = MyPagination


class HumanListView(ListAPIView):
    queryset = models.Human.objects.all()
    serializer_class = serializers.HumanListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['status', 'information', 'house']
    search_fields = ['fullname']
    pagination_class  = MyPagination



# -------------------------------------------------------------------------------------------


class ChairmanDetailView(RetrieveUpdateDestroyAPIView):
    queryset = models.Chairman.objects.all()
    serializer_class = serializers.ChairmanDetailSerializer


class MFYDetailView(RetrieveUpdateDestroyAPIView):
    queryset = models.MFY.objects.all()
    serializer_class = serializers.MFYDetailSerializer


class NeighborhoodDetailView(RetrieveUpdateDestroyAPIView):
    queryset = models.Neighborhood.objects.all()
    serializer_class = serializers.NeighborhoodDetailSerializer


class HouseDetailView(RetrieveUpdateDestroyAPIView):
    queryset = models.House.objects.all()
    serializer_class = serializers.HouseDetailSerializer


class HumanDetailView(RetrieveUpdateDestroyAPIView):
    queryset = models.Human.objects.all()
    serializer_class = serializers.HumanDetailSerializer
    
