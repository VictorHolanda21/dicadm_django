from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'restrito/$', views.restricted, name="restricted"),
    url(r'entrar/$', views.user_login, name="user_login"),
    url(r'sair/$', views.user_logout, name="user_logout"),
    url(r'registrar/$', views.register, name="register"),
]
