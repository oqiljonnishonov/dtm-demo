from rest_framework import serializers
from django.forms import ValidationError
from  djangorestapp.models import User,PhoneOTP


# class ActorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Actor
#         fields=('id','first_name','last_name','gender')
        
#         def validate_birthdate(self,data):
#             if data<data.fromisoformat('1950-01-01'):
#                 raise ValidationError(detail="Incorrect Data")
#             return data
        

# class MovieSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Movie
#         fields=('id','name','genre','year','actor')


class ValidatePhoneSendOTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneOTP
        fields = ('phone',)

class ValidateOTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneOTP
        fields = ('phone', 'otp',)

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('phone','password')
        extra_kwargs={'password':{'write_only':True}}

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','phone')

# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Comment
#         fields=('id','comment','created_at','movie','user')

# class PostCommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Comment
#         fields=('id','comment','created_at','movie')