from re import template
from unicodedata import name
from django.shortcuts import render
from django.views import generic

from .models import Artist, Album, Track

class IndexView(generic.ListView):
    template_name = 'disks/index.html'
    context_object_name = 'all_disks_list'

    def get_queryset(self):
        # Return all the albums, ordered by title in alphabetical order
        return Album.objects.order_by('title')

class DetailView(generic.DetailView):
    model = Album
    template_name = "disks/detail.html"
    def get_queryset(self):
        return Album.objects

class SearchResultsView(generic.ListView):
    model = Album
    template_name = 'disks/search_results.html'
    context_object_name = 'found_album_list'
    
    def get_queryset(self):
        user_search = self.request.GET.get("search")
        return Album.objects.filter(title__icontains=user_search).order_by('title')
    
    