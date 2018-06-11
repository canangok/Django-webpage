"""houseofapps URL Configuration

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
from django.conf.urls import include,url
from django.contrib import admin
from houseofapps.settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from houseofapps.hackathon.views import hackathon_view,send_mail
from houseofapps.settings import STATIC_URL, STATIC_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('houseofapps.main.urls')),
    url(r'hackathon/', include('houseofapps.hackathon.urls')),
    url(r'hackathon/$', hackathon_view),



]+ static(MEDIA_URL, document_root=MEDIA_ROOT)
