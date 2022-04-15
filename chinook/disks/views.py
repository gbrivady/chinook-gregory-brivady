from django.shortcuts import render
from django.views import generic

from .models import Artist, Album, Track

class IndexView(generic.ListView):
    template_name = 'disks/index.html'
    context_object_name = 'all_disks_list'

    def get_queryset(self):
        # Return all the albums, ordered by title in alphabetical order
        return Album.objects.order_by('title')
