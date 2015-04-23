from django.conf.urls import patterns, include, url
from django.contrib import admin
import core.views as coreviews

urlpatterns = patterns('',

 url(r'^$', coreviews.LandingView.as_view()),
 url(r'locations/$', coreviews.LocationListView.as_view()),
 url(r'locations/(?P<pk>\d+)/detail/$', coreviews.LocationDetailView.as_view(), name='locations_list'),
 url(r'location/create/$', coreviews.LocationCreateView.as_view()),
 url(r'search/$', coreviews.SearchListView.as_view()),
url(r'locations/(?P<pk>\d+)/update/$', coreviews.LocationUpdateView.as_view(), name='location_update'),
 
)