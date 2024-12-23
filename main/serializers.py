from main import models
from rest_framework.serializers import ModelSerializer, SlugRelatedField









class ChairmanSerializer(ModelSerializer):
    class Meta:
        model = models.Chairman
        fields = '__all__'

# -------------------------------------------------------------------------------------------

class MFYSerializer(ModelSerializer):
    chairman = SlugRelatedField(slug_field = 'name', read_only=True)
    class Meta:
        model = models.MFY
        fields = '__all__'
# -------------------------------------------------------------------------------------------


class NeighborhoodSerializer(ModelSerializer):
    MFY = SlugRelatedField(slug_field = 'title', read_only=True)
    class Meta:
        model = models.Neighborhood
        fields = '__all__'

# -------------------------------------------------------------------------------------------

class HouseSerializer(ModelSerializer):
    neighborhood = SlugRelatedField(slug_field = 'title', read_only=True)
    class Meta:
        model = models.House
        fields = '__all__'
# -------------------------------------------------------------------------------------------


class HumanSerializer(ModelSerializer):
    house = SlugRelatedField(slug_field = 'house_number', read_only=True)
    class Meta:
        model = models.Human
        fields = '__all__'

# -------------------------------------------------------------------------------------------

