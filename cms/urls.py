from django.conf.urls import patterns, url, include
from cms import views

urlpatterns = patterns(
    '',
    url(r'^faq/$', views.faq, name="faq"),
)
