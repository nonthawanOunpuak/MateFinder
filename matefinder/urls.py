"""matefinder URL Configuration

The urlpatterns list routes URLs to views. For more information please see:
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

from django.conf.urls import url
from django.contrib import admin
from .views import about, contact, login, home, signup, logout, dormCreate, storeDorm, createDorm
from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='login'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('about', views.about, name='about'),
    path('signup', views.signup, name='signup'),
    path('home', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('dorm-create', views.dormCreate, name='dorm-create'),
    path('home', views.viewPostDorm, name='viewPost'),


    path('store', views.storeDorm, name='store'),
    path('post', views.createDorm, name='post'),

    path('<studentlink>', views.profile, name='profile'),
]
