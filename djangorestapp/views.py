from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

from  djangorestapp.models import User,PhoneOTP 
from djangorestapp.serializers import ValidatePhoneSendOTPSerializer,ValidateOTPSerializer,CreateUserSerializer,UserSerializer
from django.http import Http404
from rest_framework import status

from django.contrib.auth.hashers import make_password
from rest_framework.permissions import AllowAny, IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
import random


# class ActorAPIView(APIView):
#     serializer_class=ActorSerializer
#     permission_classes = (AllowAny,)
#     @swagger_auto_schema(request_body=ActorSerializer)
#     def post(self,request):
#         serializer=ActorSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response('Cant posted !')
        
#     def get(self,request):
#         actors=Actor.objects.all()
#         serializer=ActorSerializer(actors,many=True)
#         return Response(data=serializer.data)

# class MovieAPIView(APIView):
#     serializer_class=MovieSerializer
#     permission_classes = (AllowAny,)
#     @swagger_auto_schema(request_body=MovieSerializer)
#     def post(self,request):
#         serializer=MovieSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response('Cant posted !')
    
#     def get(self,request):
#         movies=Movie.objects.all()
#         serializer=MovieSerializer(movies,many=True)
#         return Response(data=serializer.data)

# class GetMovieAPIView(APIView):
#     permission_classes = (AllowAny,)
    
#     def get(self,request,pk):
#         movie=Movie.objects.get(pk=pk)
#         serializer=MovieSerializer(movie)
#         return Response(data=serializer.data)

# class CommentListAPIView(APIView):
#     serializer_class=PostCommentSerializer
#     permission_classes = (IsAuthenticated,)
#     @swagger_auto_schema(request_body=PostCommentSerializer)
#     def post(self,request):
        
#         # print(f'requessttt: {request.data}***{request.user.id}')
#         serializer=PostCommentSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer_obj = serializer
#             serializer_obj.save(user=request.user)
            
#             # comment_id=serializer_obj.data.get('id')
#             # comment=Comment.objects.get(pk=comment_id)
#             # comment.user.add((request.user.id))
#             # comment.save()
#             return Response('Comment Successfuly Posted !')
#         else:
#             return Response('Comment Unsuccessfuly !')
    
#     def get(self,request):
#         queryset=Comment.objects.filter(user=request.user)
#         serializer_class=CommentSerializer(queryset,many=True)
#         return Response(serializer_class.data)


# class GetUserCommentsAPIView(APIView):
#     serializer_class=UserSerializer
#     permission_classes = (IsAuthenticated,)
    
#     def get(self,request):
#         # user_id=request.data.get('id')
#         # comments=Comment.user.get_object(user_id)
#         queryset=Comment.objects.filter(user=request.user)
#         serializer_class=CommentSerializer(queryset,many=True)
#         return Response(serializer_class.data)
#         # return Response(comments.data)
# # class PutCommentAPIView(APIView): #Update comment
# #     permission_classes = (IsAuthenticated,)

# #     def put(self, request, id):
# #         comment=request.data.get('comment')
# #         query = Comment.objects.get(id=id)
# #         if query:
# #             query.comment = comment
# #             query.save()
# #             return Response('Successfuly Updated')
# #         else:
# #             return Response('no abject')


#Auth:

class ValidatePhoneSendOTP(APIView):
    permission_classes=(AllowAny,)
    
    @swagger_auto_schema(request_body=ValidatePhoneSendOTPSerializer)
    def post(self,request):
        phone_number=request.data.get('phone')
        if phone_number:
            phone=str(phone_number)
            user=User.objects.filter(phone__iexact=phone)
            if user.exists():
                return Response(
                    {
                        'status':False,
                        'detail':'this phone number already exist !',
                    }
                )
            else:
                key=send_otp(phone)
                if key:
                    old=PhoneOTP.objects.filter(phone__iexact=phone)
                    if old.exists():
                        old.first()
                    PhoneOTP.objects.create(phone=phone,otp=key)
                    return Response(
                        {
                            'status':True,
                            'detail':'OTP sent successfully !',
                        }
                    )
                else:
                    return Response(
                        {
                            'status':False,
                            'detail':'sending otp error !',
                        }
                    )
        else:
            return Response(
                {
                    'status':False,
                    'detail':'phone number is not given post request !'
                }
            )

def send_otp(phone):
    if phone:
        key = random.randint(99999, 999999)
        print(key)
        return key
    else:
        return False

class ValidateOTP(APIView):
    permission_classes=(AllowAny,)
    
    @swagger_auto_schema(request_body=ValidateOTPSerializer)
    def post(self,request):
        phone=request.data.get('phone',False)
        otp_send=request.data.get('otp',False)
        
        if phone and otp_send:
            old=PhoneOTP.objects.filter(phone__iexact=phone)
            if old.exists():
                old=old.first()
                otp=old.otp
                if str(otp_send)==str(otp):
                    old.validated=True
                    old.save()
                    return Response(
                        {
                            'status':True,
                            'detail':'OTP matched. Please proceed for registration !',
                        }
                    )
                else:
                    return Response(
                        {
                            'status':False,
                            'detail':'OTP INCORRECT !',
                        }
                    )
            else:
                return Response(
                    {
                        'status':False,
                        'detail':'First proceed via sending otp request !',
                    }
                )
        else:
            return Response({
                'status': False,
                'detail': 'please provide both phone and OTP for validation !',
            })


class Register(APIView):
    permission_classes=(AllowAny,)
    
    @swagger_auto_schema(request_body=CreateUserSerializer)
    def post(self,request):
        phone=request.data.get('phone',False)
        password=request.data.get('password',False)
        username=request.data.get('username',False)
        if phone and password:
            old=PhoneOTP.objects.filter(phone__iexact=phone)
            if old.exists():
                old=old.first()
                validated=old.validated
                data=request.data
                if validated:
                    reg_serializer=CreateUserSerializer(data=data)
                    if reg_serializer.is_valid():
                        password=reg_serializer.validated_data.get('password')
                        reg_serializer.validated_data['password']=make_password(password)
                        new_user=reg_serializer.save()
                        old.delete()
                        return Response(
                            {
                                'status':True,
                                'detail':'Account successfuly created !'
                            }
                        )
                    else:
                        return Response(
                            {
                                'status':False,
                                'detail':"OTP haven't verified .First do that step !"
                            }
                        )
                        
            else:
                return Response(
                    {
                        'status':False,
                        'detail':'please verify phone first !',
                    }
                )
        else:
            return Response(
                {
                    'status': False,
                    'datail': "Both Phone and password are not sent !",
                }
            )