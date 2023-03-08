from django.urls import path,include
from djangorestapp.views import ValidatePhoneSendOTP,ValidateOTP,Register





urlpatterns = [
    path('validate_phone/', ValidatePhoneSendOTP.as_view(), name='validate_phone'),
    path('validate_otp/', ValidateOTP.as_view(), name='validate_otp'),
    path('register/', Register.as_view(), name='register'),
    
    # path('delete/<int:id>', PutCommentAPIView.as_view(), name='Update'),
    # path('CommentList/', CommentListAPIView.as_view(), name='CommentList'),
    # path('getusercomment/',GetUserCommentsAPIView.as_view()),
    # path('actors/',ActorAPIView.as_view(),name='Actors'),
    # path('movies/',MovieAPIView.as_view(),name='Movies'),
    # path('detmovie/<int:pk>',GetMovieAPIView.as_view(),name='GetMovie')

]