from django.conf.urls import url
from .views import *

urlpatterns = [
	#My homepage
	url(r'^$', index, name='index'),

]