from rest_framework import serializers
from .models import *
class PolygonField(serializers.Field):
    def to_representation(self, value):
        # Serialize a Polygon object as a dictionary with "type" and "coordinates" fields
        return {
            "type": "Polygon",
            "coordinates": value.coords[0]
        }

    def to_internal_value(self, data):
        # Deserialize a dictionary with "type" and "coordinates" fields as a Polygon object
        return GEOSGeometry(json.dumps(data))
      
class AmenitiesSerializer(serializers.ModelSerializer):
  class Meta:
    model: Amenities
    fields = '__all__'

class BuildingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buildings
        fields = '__all__'

class ForestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forest
        fields = '__all__'

class WaterBodySerializer(serializers.ModelSerializer):
  distance = serializers.FloatField()
  class Meta:
    model: Waterbody
    fields = '__all__'

class RoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Road
        fields = '__all__'