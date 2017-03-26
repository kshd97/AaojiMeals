from django.conf.urls import url

from . import views

app_name='Login'

urlpatterns = [
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^signup/$', views.signup, name='signup'),
]