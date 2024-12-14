from main import models
from rest_framework.serializers import ModelSerializer, SlugRelatedField



class ChairmanListSerializer(ModelSerializer):
    class Meta:
        model = models.Chairman
        fields = ['id','name']


class MFYListSerializer(ModelSerializer):
    class Meta:
        model = models.MFY
        fields = ['id','title']


class NeighborhoodListSerializer(ModelSerializer):
    class Meta:
        model = models.Neighborhood
        fields = ['id','title']


class HouseListSerializer(ModelSerializer):
    class Meta:
        model = models.House
        fields = ['id','house_number', 'a_b']


class HumanListSerializer(ModelSerializer):
    class Meta:
        model = models.Human
        fields = ['id','fullname']



# ------------------------------------------------------------------------------------------



class ChairmanDetailSerializer(ModelSerializer):
    class Meta:
        model = models.Chairman
        fields = '__all__'


class MFYDetailSerializer(ModelSerializer):
    chairman = SlugRelatedField(slug_field = 'name', read_only=True)
    class Meta:
        model = models.MFY
        fields = '__all__'


class NeighborhoodDetailSerializer(ModelSerializer):
    MFY = SlugRelatedField(slug_field = 'title', read_only=True)
    class Meta:
        model = models.Neighborhood
        fields = '__all__'


class HouseDetailSerializer(ModelSerializer):
    neighborhood = SlugRelatedField(slug_field = 'title', read_only=True)
    class Meta:
        model = models.House
        fields = '__all__'


class HumanDetailSerializer(ModelSerializer):
    house = SlugRelatedField(slug_field = 'house_number', read_only=True)
    class Meta:
        model = models.Human
        fields = '__all__'


