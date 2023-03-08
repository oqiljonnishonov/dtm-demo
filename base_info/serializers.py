from rest_framework import serializers
# from django.forms import ValidationError

from base_info.models import Citizenship , States , Regions , Districts , InstitutionType , Institutions

class CitizenshipSerializer(serializers.ModelSerializer):
    class Meta:
        model=Citizenship
        fields=('citizens',)

class StatesSerializer(serializers.ModelSerializer):
    class Meta:
        model=States
        fields=('state',)

class RegionsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Regions
        fields=('region',)

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model=Districts
        fields=('district',)

class InstitutionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=InstitutionType
        fields=('type',)

class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Institutions
        fields=('institution',)