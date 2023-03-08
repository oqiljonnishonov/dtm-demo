from rest_framework import serializers
from personal_info.models import PersonalInfo , PermamentAddress , GraduatedEdu

class PostPersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=PersonalInfo
        fields=('id','citizenship','jshshir','passport_series','passport_num','first_name','last_name','surname','birth_date')

class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=PersonalInfo
        fields=('id','citizenship','jshshir','passport_series','passport_num','first_name','last_name','surname','birth_date','user')

class PostPermamentAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=PermamentAddress
        fields=('id','region','district','address')

class PermamentAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=PermamentAddress
        fields=('id','region','district','address','user')

class PostGraduatedEduSerializer(serializers.ModelSerializer):
    class Meta:
        model=GraduatedEdu
        fields=('id','state','region','district','graduate_institution_type','graduate_institution','graduated_date','doc_ser_num')

class GraduatedEduSerializer(serializers.ModelSerializer):
    class Meta:
        model=GraduatedEdu
        fields=('id','state','region','district','graduate_institution_type','graduate_institution','graduated_date','doc_ser_num','user')
