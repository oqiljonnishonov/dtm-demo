from django.urls import path
from base_info.views import CitizenAPIView




urlpatterns = [
    path('citizens/',CitizenAPIView.as_view(),name='Citizens')
]
