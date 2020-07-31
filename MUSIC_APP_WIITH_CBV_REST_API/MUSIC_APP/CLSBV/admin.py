from django.contrib import admin
from .models import Musician,Album


@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    fields          = ['first_name','last_name','instrument']
    list_display    = ['first_name','last_name','instrument']
    list_filter     = ['first_name','last_name','instrument']
    search_fields   = ['first_name','last_name','instrument']


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    fields          = ['artist','name','release_date','num_starts']
    list_display    = ['artist','name','release_date','num_starts']
    list_filter     = ['artist','name','release_date','num_starts']
    search_fields   = ['artist','name','release_date','num_starts']
