"""ServidorCalendar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from Calendar import views


urlpatterns = [
	url(r'^registro/', views.registro),
	url(r'^registrar/', views.registrar),
	url(r'^login/', views.login),
	url(r'^validacion/', views.validacion),
	url(r'^calendario/', views.calendario),
    url(r'^evento/', views.evento),
    url(r'^creacion/', views.creacion),
    url(r'^eliminar/', views.eliminar),
	url(r'^logout/', views.logout),
    url(r'^admin/', admin.site.urls),
]
