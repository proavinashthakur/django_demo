from rest_framework import serializers
from . models import Countries, Continents, Cities, Plan


class ContinentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Continents
        fields = "__all__"


class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = "__all__"


class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = "__all__"


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"