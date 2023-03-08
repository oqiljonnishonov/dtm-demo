from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from djangorestapp.models import User

from personal_info.models import PersonalInfo , PermamentAddress , GraduatedEdu
from personal_info.serializers import (PersonalInfoSerializer ,PostPersonalInfoSerializer , 
                                       PermamentAddressSerializer ,PostPermamentAddressSerializer , 
                                       GraduatedEduSerializer , PostGraduatedEduSerializer)

from rest_framework.permissions import IsAuthenticated

# Create your views here.

class PersonalInfoAPIView(APIView):
    serializer_class=PostPersonalInfoSerializer
    permission_classes=(IsAuthenticated,)
    
    def post(self,request):
        serializer=PostPersonalInfoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer_obj=serializer
            serializer_obj.save(user=request.user)
            return Response('Comment successfully posted !')
        else:
            return Response("Can't posted !")
    
    def get(self,request):
        queryset=PersonalInfo.objects.filter(user=request.user)
        serializer_class=PersonalInfoSerializer(queryset,many=True)
       
        return Response(serializer_class.data)
    
    def put(self,request):
        queryset=PersonalInfo.objects.filter(user=request.user).first()
        person_info=PostPersonalInfoSerializer(data=request.data , instance=queryset)
        if person_info.is_valid(raise_exception=True):
            personal_obj=person_info
            personal_obj.save(user=request.user)
            return Response(personal_obj.data)
        else:
            return Response("Can't Updated !")
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc2MzQ1OTYyLCJpYXQiOjE2NzYyOTc5NjIsImp0aSI6Ijk1MGI4YjVkNDYxZDQzMDdhNzQ4NjYzM2I2YjJkZWZjIiwidXNlcl9pZCI6MX0.5yVcOQUNEL6YrqJyNX8rkbAqiWLjz0eyfuxd7Id_ddI
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc2MzQ2ODc2LCJpYXQiOjE2NzYyOTg4NzYsImp0aSI6IjFlZDc5ODNmNGUwYjQ3NDI5MWY4Nzc2MjhiNzdmMDUxIiwidXNlcl9pZCI6Mn0.QR_1pQE9b-DgVTbye6JUq0nkMUZFUE1yVHb6ot6SY1U

# {
#     "citizenship": 1,
#     "jshshir": "21345678912345",
#     "passport_series": "AB",
#     "passport_num": "2134567",
#     "first_name": "Oqiljon",
#     "last_name": "Islomov",
#     "surname": "Erkinjon o'g'li",
#     "birth_date": "2000-02-02"
# }

class PermamentAddreessAPIView(APIView):
    serializer_class=PostPermamentAddressSerializer
    permission_classes=(IsAuthenticated,)
    
    def post(self,request):
        serializer=PostPermamentAddressSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer_obj=serializer
            serializer_obj.save(user=request.user)
            return Response('Comment successfully posted !')
        else:
            return Response("Can't posted !")
    
    def get(self,request):
        queryset=PermamentAddress.objects.filter(user=request.user)
        serializer_class=PermamentAddressSerializer(queryset,many=True)
        return Response(serializer_class.data)
    
    def put(self,request):
        queryset=PermamentAddress.objects.filter(user=request.user).first()
        address_info=PostPermamentAddressSerializer(data=request.data, instance=queryset)
        
        if address_info.is_valid(raise_exception=True):
            address_obj=address_info
            address_obj.save(user=request.user)
            return Response(address_obj.data)
        else:
            return Response("Can't Updated !")

class GraduatedEduAPIView(APIView):
    serializer_class=PostGraduatedEduSerializer
    permission_classes=(IsAuthenticated,)
    
    def post(self,request):
        serializer=PostGraduatedEduSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer_obj=serializer
            serializer_obj.save(user=request.user)
            return Response('Comment successfully posted !')
        else:
            return Response("Can't posted !")
    
    def get(self,request):
        queryset=GraduatedEdu.objects.filter(user=request.user)
        serializer_class=GraduatedEduSerializer(queryset,many=True)
        return Response(serializer_class.data)
    
    def update(self,request):
        queryset=GraduatedEdu.objects.filter(user=request.user).first()
        graduated_info=PostGraduatedEduSerializer(data=request.data , instance=queryset)
        
        if graduated_info.is_valid(raise_exception=True):
            graduated_obj=graduated_info
            graduated_obj.save(user=request.user)
            return Response(graduated_obj.data)
        else:
            return Response("Can't Updated !")
