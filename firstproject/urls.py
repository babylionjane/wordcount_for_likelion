from django.conf.urls import url
from django.contrib import admin

from wordcount import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name="home"),
    url(r'^about/$', views.about, name='about'),
    url(r'^result/$', views.result, name='result'),
]
