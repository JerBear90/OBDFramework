from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
	url(r'^$', views.home),
	# url(r'^guagetwo/$', views.guagetwo, name='guagetwo'),
	url(r'^rpm/$', views.rpm, name='rpm'),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
