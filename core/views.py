from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
import core.models as coremodels

# Create your views here.

class LandingView(TemplateView):
    template_name = "base/index.html"

class LocationListView(ListView):
    model = coremodels.Location
    template_name = 'location/list.html'

class LocationDetailView(DetailView):
    model = coremodels.Location
    template_name = 'location/detail.html'
    context_object_name = 'location'
    
class LocationCreateView(CreateView):
  model = coremodels.Location
  template_name = 'base/form.html'
  fields = "__all__"