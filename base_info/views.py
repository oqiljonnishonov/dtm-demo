from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

from base_info.models import  Citizenship , States , Regions , Districts , InstitutionType , Institutions
from base_info.serializers import CitizenshipSerializer , StatesSerializer , RegionsSerializer , DistrictSerializer , InstitutionTypeSerializer , InstitutionSerializer

from rest_framework.permissions import IsAdminUser 



class CitizenAPIView(APIView):
    serializer_class=CitizenshipSerializer
    permission_classes=(IsAdminUser,)
    
    def post(self,request):
        serializer=CitizenshipSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Comment successfully posted !')
        else:
            return Response("Can't posted !")
    
    def get(self,request):
        citizens=Citizenship.objects.all()
        serializer=CitizenshipSerializer(citizens,many=True)
        return Response(data=serializer.data)

