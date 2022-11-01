from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^Get_Gender_Bar/$',Get_Gender_Bar,name="Get_Gender_Bar"),
	url(r'^Verified_Login/$',Verified_Login,name="Verified_Login"),
	url(r'^Save_Song/$',Save_Song,name="Save_Song"),
	url(r'^Get_List_Song/$',Get_List_Song,name="Get_List_Song"),
	url(r'^Delete_Music/$',Delete_Music,name="Delete_Music"),
]