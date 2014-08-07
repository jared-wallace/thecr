from django.conf.urls import patterns, url, include
from about import views

urlpatterns = patterns(
    '',
    url(r'^worship-team/$', views.worship, name="worship"),
)
