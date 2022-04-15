from operator import mod
from django.db import models

class Artist(models.Model):
    """
    An artist that may have some albums
    """
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Album(models.Model):
    """
    An album by one artist with several tracks
    """
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    
class Track(models.Model):
    """
    A single track in an album
    """
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=200)
    composer = models.CharField(max_length=200)
    milliseconds = models.IntegerField('Duration (ms)')
    bytes = models.IntegerField('Size (bytes)')
    unitPrice = models.DecimalField('Unit Price (EUR)', max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name