from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^upload$', views.upload, name='upload'),
    url(r'^user$', views.auth, name='user'),
    url(r'^users$', views.UserList.as_view(), name='user'),
]
