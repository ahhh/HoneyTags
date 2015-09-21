from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^.*/$', views.index, name='index'),
	url(r's', views.callback, name='callback'),
	url(r'dump', views.dump, name='dump'),
	url(r'add', views.regTag, name='regTag'),
	url(r'', views.index, name='index'),
#	url(r'^admin/', include(admin.site.urls)),
]
