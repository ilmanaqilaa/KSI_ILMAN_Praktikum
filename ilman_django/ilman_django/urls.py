
from django.contrib import admin
from django.urls import include, path, re_path
from django.http import HttpResponse

from . import views

from blog.views import index

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('about/', include('about.urls', namespace='about')),
    path('form/', views.form, name='form'),
    re_path(r'^articles/(?P<year>[0-9]{4})/$', views.articles, name='dinamis'),
    re_path(r'^delete/(?P<year>[0-9]+)/$', views.delete, name='delete'),
    re_path(r'^update/(?P<year>[0-9]+)/$', views.update, name='update'),

    path('', index),
    ]
