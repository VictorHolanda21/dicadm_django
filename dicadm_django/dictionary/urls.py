
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'termos/$', views.index, name="index"),
    url(r'termos/adicionar/$', views.add_word, name="add_word"),
    url(r'termos/(?P<slug>[\w-]+)/$', views.detail, name="detail"),
    url(r'categoria/$', views.show_category, name="show_category"),
    url(r'categoria/adicionar/$', views.add_category, name="add_category"),
    url(r'categoria/(?P<slug>[\w-]+)/$', views.show_category, name="show_category"),
]
