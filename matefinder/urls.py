from django.conf.urls import url
from django.contrib import admin
from .views import about, contact,blog,home,profile, login, register

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about$', about, name='about'),
    url(r'^contact$', contact, name='contact'),
    url(r'^blog$', blog, name='blog'),
    url(r'^home$', home, name='home'),
    url(r'^profile$', profile, name='profile'),
    url(r'^login$', login, name='login'),
    url(r'^register$', register, name='register'),
]
