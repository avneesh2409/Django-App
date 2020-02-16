"""mymodel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.conf.urls import include, url
from .views import *
#from rest_framework import routers
#from .registerSerializer import RegisterViewSet

#router = routers.DefaultRouter()
#from customers import views
#router.register(r'register', RegisterViewSet)

urlpatterns = [
   url(r'^$',index,name='index'),
   url(r'^api/$', customers_list,name="customer_list"),
   url(r'^api/(?P<pk>[0-9]+)$', customers_detail,name="customer_detail"),
  # url(r'api/', include(router.urls))
]
