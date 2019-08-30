from django.contrib.auth.models import *
from rest_framework import viewsets, permissions, status, generics, views
from polls.serializers import *
from django.utils import timezone

from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from .permissions import *
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from django.core.files.storage import FileSystemStorage
import random

from django.views.decorators.csrf import csrf_exempt
import requests
from rest_framework import filters
from django_filters import rest_framework as djfilters

from knox.views import LoginView as KnoxLoginView
from knox.auth import TokenAuthentication

from django.contrib.auth import login
# from google.cloud import storage


class ValidatePhoneSendOtp(views.APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')

        if phone_number:
            phone_number = str(phone_number)
            user = User.objects.filter(username=phone_number)
            if user.exists():
                return Response({
                    'status' : False,
                    'detail' : 'Phone Number already exists'
                })
            else :
                print(phone_number)
                key = send_otp(phone_number)
                if key:
                    old = PhoneOTP.objects.filter(phone_number__iexact = phone_number)
                    if old.exists():
                        old = old.first()
                        count = old.count
                        if count > 10:
                            return Response({
                            'status' : False,
                            'detail' : 'Sending OTP Error. Limit Exceeded.Please contact Customer Support'
                                })

                        old.count =  count + 1
                        old.otp = key
                        old.save()  
                        return Response({
                        'status' : True,
                        'detail' : 'OTP send successfully!!'
                        })  

                    else:
                        PhoneOTP.objects.create(
                            phone_number = phone_number,
                            otp = key,
                        )
                        return Response({
                            'status' : True,
                            'detail' : 'OTP send successfully!!'
                            })
                else:
                    return Response({
                        'status' : False,
                        'detail' : 'Sending OTP error'
                    })
        
        else:
             return Response({
                'status' : False,
                'detail' : 'Phone Number is not given!'
            })

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

class ValidateOTP(views.APIView):
    """
    If user have received the OTP, he/she will post a request with phone and that OTP and then the user 
    will be direct to set the password.
    """
    permission_classes = [permissions.AllowAny]
    def post(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')
        otp_sent = request.data.get('otp')

        if phone_number and otp_sent:
            old = PhoneOTP.objects.filter(phone_number__iexact = phone_number).order_by('created_at')
            if old.exists():
                old = old[0]
                if str(otp_sent) == str(old.otp):
                    old.is_verified = True
                    old.save()
                    return Response({
                        'status' : True,
                        'detail' : 'OTP Matched.Please proceed for Registration',
                        })
                else:
                    return Response({
                        'status' : False,
                        'detail' : 'OTP Incorrect'
                    })            
            else:
                return Response({
                    'status' : False,
                    'detail' : 'First verify your Phone number'
                })

        else:
            return Response({
                'status' : False,
                'detail' : 'Please provide both Phone number and OTP'
            })



class CommenViewSet(viewsets.ModelViewSet):
	permission_classes  = (permissions.AllowAny,)
	filter_backends = (filters.OrderingFilter,filters.SearchFilter,djfilters.DjangoFilterBackend,)
	filterset_fields = '__all__'
	search_fields = '__all__'
	ordering_fields = '__all__'
	extra_permissions = None
	def get_permissions(self):
		"""
		Instantiates and returns the list of permissions that this view requires.
		"""
		extra = []
		if self.extra_permissions is not None:
			extra = [permission() for permission in self.extra_permissions]
		return [permission() for permission in self.permission_classes]+extra


# class VerifyViewSet(CommenViewSet):
# 	queryset = Verify.objects.filter(archived=False)
# 	serializer_class = VerifySerializer
# 	def retrieve(self, request, pk=None):
# 		verify = Verify.objects.get(code = pk)
# 		verify.verified = True
# 		verify.save()
# 		serializer = VerifySerializer(verify)
# 		return Response(serializer.data)	

class UserViewSet(CommenViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	filterset_fields = ('username', 'email')
	search_fields = ('username', 'email')

class Custom_UserViewSet(CommenViewSet):
	queryset = Custom_User.objects.all()
	serializer_class = Custom_UserSerializer


class PollViewSet(CommenViewSet):
    queryset = Question.objects.all()
    serializer_class = PollSerializer


class ChoiceViewSet(CommenViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class TextAnswerViewSet(CommenViewSet):
    queryset = TextAnswer.objects.filter(approved=True)
    serializer_class = TextAnswerSerializer
    read_only_fields = ('approved',)

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super().post(request, format=None)
