from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CommenInfo(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	

class Custom_User(CommenInfo):
	gender = models.CharField(max_length = len("transgender"), blank=True, null=True)
	user = models.OneToOneField (
        User,
        on_delete=models.CASCADE,
    )
	image = models.URLField(blank=True, null=True)
	

	def __str__(self):
		return "Phone:{}".format(self.user.username)

	class Meta:
		verbose_name = "Custom User"
		verbose_name_plural = "Custom Users"



class Question(CommenInfo):
	type_of_poll = ((0,'MCQ'),
		(1,'TEXT'),
		)
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField(auto_now_add=True)
	poll_image = models.URLField()
	background_color = models.CharField(max_length=8)
	poll_type = models.IntegerField(choices=type_of_poll, default=0)
	poll_orderid_1 = models.IntegerField(default=0)
	poll_orderid_2 = models.IntegerField(default=0)
	poll_orderid_3 = models.IntegerField(default=0)
	public = models.BooleanField(default=True)
	anonymous_user = models.BooleanField(default=False)

	user = models.ForeignKey (
        User,
        default=0,
        on_delete=models.CASCADE,
    )	
	
	
	def __str__(self):
		return self.question_text


class Choice(CommenInfo):
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	poll = models.ForeignKey (
        Question,
        on_delete=models.CASCADE,
    )	
	def __str__(self):
		return self.choice_text

class TextAnswer(CommenInfo):
	answer = models.TextField(default='Answer')
	poll = models.ForeignKey (
        Question,
        on_delete=models.CASCADE,
		default=0,
    )
	approved = models.BooleanField(default=False)	

# class Responders(CommenInfo):
# 	responder = models.ForeignKey (
#         User,
#         default=0,
#         on_delete=models.CASCADE,
#     )
# 	poll = models.ForeignKey(
# 		Question,
# 		on_delete = models.CASCADE
# 		)

class PhoneOTP(CommenInfo):
    # phone_regex     = RegexValidator(regex=r'^\+?1?\d{9,14}$', message="Phone number must be entered in the format: '999999999'")
    phone_number    = models.CharField(verbose_name='phone_number', unique=True, max_length=15, blank=True, help_text="Phone number to be validated") # validators should be a list
    otp             = models.CharField(verbose_name='OTP', max_length=6, help_text="otp to be send to the Phone number")
    count           = models.IntegerField(verbose_name='Attempted count', default=0, help_text='Number of OTP send.')
    is_verified     = models.BooleanField(verbose_name='is_verified', default=False, help_text='If it is true, this means user has validated otp correctly')

    def __str__(self):
        return "%s" %(self.phone_number)
