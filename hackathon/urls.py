from django.conf.urls import url
from . import views

urlpatterns = [


    url(r'^send_mail_hackathon/$', views.send_mail_hackathon, name='send_mail_hackathon'),

]
