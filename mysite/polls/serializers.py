
from django.contrib.auth.models import *
from rest_framework import serializers
from .models import *
import random
import datetime


def send_otp(phone_number):
    if phone_number:
        key = random.randint(999,9999)
        api_key = "9b14b538-19c1-11e9-9ee8-0200cd936042"
        link = f"https://2factor.in/API/V1/{api_key}/SMS/{phone_number}/{key}"
        payload = ""
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.request("GET", link, data=payload, headers=headers)
        print (key)
        print(response.text)
        return key
    else :
        return False

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('email', 'first_name', 'last_name','password','username',)
		extra_kwargs = {'password': {'write_only': True}}

	def create(self, validated_data):
		password = validated_data.pop('password')
		username = validated_data.pop('username')
		if not User.objects.filter(username =username).exists():
			if PhoneOTP.objects.filter(phone_number =username,is_verified=True).exists():
				user, created = User.objects.get_or_create(username = username,**validated_data)
				user.set_password(password)
				user.save()
				return user
			raise serializers.ValidationError("Phone number not verified")		
		raise serializers.ValidationError("Same Phone")



class Custom_UserSerializer(serializers.ModelSerializer):
	user = UserSerializer(required = True)
	class Meta:
		model = Custom_User
		fields = '__all__'
		read_only_fields = ('archived',)

	def create(self, validated_data):
		user_data = validated_data.pop('user')
		user = UserSerializer.create(UserSerializer(), validated_data=user_data)
		custom_user, created = Custom_User.objects.update_or_create(user=user,**validated_data)
		return custom_user

class PollSerializer(serializers.ModelSerializer):
	class Meta:
		model = Question
		fields = '__all__'

class ChoiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Choice
		fields = '__all__'

class TextAnswerSerializer(serializers.ModelSerializer):
	class Meta:
		model = TextAnswer
		fields = '__all__'
		
	