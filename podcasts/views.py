from django.shortcuts import render
from django.views.generic import ListView
from .models import Episode

# Create your views here.
#inheriting from the ListView class so that you can iterate over the episodes
class HomePageView(ListView):
    template_name = 'homepage.html'
    model = Episode

#Override the context data and filter by the ten most recent episodes, as determined by the published date, pub_date.
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["episodes"] = Episode.objects.filter().order_by("-pub_date")[:30]
        return context


