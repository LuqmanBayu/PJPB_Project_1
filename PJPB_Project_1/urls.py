"""PJPB_Project_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
# from django.conf.urls import url, include
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from management_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Loginpage, name="show_login"),
    path('first/', views.SecondPage, name="first_page"),

    # path('accounts/', include('management_app.urls')),
    # path('', views.Loginpage, name="show_login"),
    # path('doLogin', views.doLogin, name="do_login"),

]
