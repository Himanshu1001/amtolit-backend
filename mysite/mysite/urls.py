from django.conf.urls import url, include
from rest_framework import routers
from polls import views
from rest_framework.documentation import include_docs_urls
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import re_path
from django.views.generic import TemplateView
from knox import views as knox_views
from polls.views import LoginAPI

router = routers.DefaultRouter()
router.register(r'custom_user', views.Custom_UserViewSet)
router.register(r'user', views.UserViewSet)
router.register(r'polls', views.PollViewSet)
router.register(r'choice', views.ChoiceViewSet)
router.register(r'answer', views.TextAnswerViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='My API title')),
    url(r'^validate_phone/', views.ValidatePhoneSendOtp.as_view(),name='validate_phone'),
	url(r'^validate_otp/', views.ValidateOTP.as_view(),name='validate_otp'),
	url(r'^', include(router.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^r/', TemplateView.as_view(template_name='index.html')),
    url(r'^login/', LoginAPI.as_view()),
    url(r'^logout/', knox_views.LogoutView.as_view())

]
