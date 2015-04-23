from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
import core.models as coremodels

# Create your views here.

class LandingView(TemplateView):
    template_name = "base/index.html"

class LocationListView(ListView):
    model = coremodels.Location
    template_name = 'location/list.html'
    
class SearchListView(LocationListView):
    def get_queryset(self):
        incoming_query_string = self.request.GET.get('query', '')
        return coremodels.Location.objects.filter(title__icontains=incoming_query_string)

class LocationDetailView(DetailView):
    model = coremodels.Location
    template_name = 'location/detail.html'
    context_object_name = 'location'
    
class LocationCreateView(CreateView):
  model = coremodels.Location
  template_name = 'base/form.html'
  fields = "__all__"

class LocationUpdateView(UpdateView):
    model = coremodels.Location
    template_name = 'base/form.html'
    fields = "__all__"

class ReviewCreateView(CreateView):
    model = coremodels.Review
    template_name = 'base/form.html'
    fields = ['description', 'rating']
  
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.location = coremodels.Location.objects.get(id=self.kwargs['pk'])
        return super(ReviewCreateView, self).form_valid(form)
        
    def get_success_url(self):
        return self.object.location.get_absolute_url()
        
class ReviewUpdateView(UpdateView):
    model = coremodels.Review
    template_name = 'base/form.html'
    fields = ['description', 'rating']
    
    def get_object(self):
        return coremodels.Review.objects.get(location__id=self.kwargs['pk'], user=self.request.user)
 
    def get_success_url(self):
        return self.object.location.get_absolute_url()