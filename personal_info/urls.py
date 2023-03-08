from django.urls import path
from personal_info.views import PersonalInfoAPIView , PermamentAddreessAPIView , GraduatedEduAPIView


urlpatterns = [
    path('personal_info/',PersonalInfoAPIView.as_view(),name='Personal Infos'),
    path('personal_address/',PermamentAddreessAPIView.as_view(),name='Permament Addresses'),
    path('graduated_edu/',GraduatedEduAPIView.as_view(),name='Graduated Educations'),
]
