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

from .views import about, contact, login, home, logout, storeDorm, createDorm

from .views import about, contact, login, home, logout, storeDorm, createDorm, viewPostDorm, createAccount, storeAccount
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('about', views.about, name='about'),

    path('signup', views.createAccount, name='signup'),
    path('storeAccount', views.storeAccount, name='storeAccount'),

    path('home', views.home, name='home'),


    path('profile_edit', views.profile_edit, name='profile_edit'),
    path('edited', views.profile_edited, name='edited'),


    path('home', views.viewPostDorm, name='viewPost'),
    path('homepage', views.viewPostDorm, name='homepage'),


    path('store', views.storeDorm, name='store'),
    path('post', views.createDorm, name='post'),
    path('delete/<int:pk>', views.deleteDorm, name='delete'),

    path('<studentlink>', views.profile, name='profile'),


]
