"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# from django.conf.urls import include, url
# from django.contrib import admin
# from community.views import *

# urlpatterns = [
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^write/', write, name='write'),
# ]

# from django.conf.urls import url
# from django.contrib import admin
# from community.views import *
from django.contrib import admin
from django.urls import path, include
from community.views import *

urlpatterns = [
    path('bbs/', list, name='list'),
    #path('bbs/view/(?P<num>[0-9]+)', view, name='view'),
    path('bbs/view/<num>/', view, name='view'),
    path('bbs/edit/<num>/', edit, name='edit'),
    path('bbs/write/', write, name='write'),
    path('admin/', admin.site.urls),
]