from django.views.generic import TemplateView, ListView, DetailView
from .models import Thing

class HomeView(TemplateView):
  template_name = 'home.html'

class ThingListView(ListView):
  template_name = 'thing_list.html'
  model = Thing
  context_object_name = 'things'

class ThingDetailView(DetailView):
  template_name = 'thing_detail.html'
  model = Thing


