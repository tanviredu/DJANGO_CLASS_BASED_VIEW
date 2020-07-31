from django.shortcuts import render
from .models import Musician,Album
from django.http import HttpResponse
from django.shortcuts import redirect,reverse
from django.views.generic import TemplateView,CreateView,UpdateView,DeleteView,DetailView,View,ListView
from .forms import AlbumForm
from django.urls import reverse_lazy
## all kinds of view

##########################################################
def index(request):
    return HttpResponse("Hello world")

## write the same thing with  class in index
## that will give the exact same result
class indexView(View):
    def get(self,request):
        return HttpResponse("hello world");


###########################################################

## template view like the render function  with context dictinory
## we use the template view with the template view function

class ViewTemplate(TemplateView):
    ## name of the index
    template_name = 'CLSBV/index.html'

    ## giving the context dictionary
    ## this is a efault function
    ## **kwargs will be  adynamic argument list baed on key value pair
    ## this is how you add the context data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)## you have to write this line
                                                    ## call the base constructoe
        context['sample_text_1'] = "This is from the index page"
        context['sample_text_2'] = "this is also from the index page"
        ## as many as you need
        return context



class ShowList(ListView):
    ## we pass a database object name that will be passed to the template
    context_object_name = "music_list"
    ## need the model
    model = Musician
    template_name = 'CLSBV/list.html'



## make another list view for the Album

class ShowAlbumList(ListView):
    context_object_name = "albumlist"
    model = Album
    template_name = 'CLSBV/album_list.html'



## make two class
## remember this class implecely take a id 

class MusicianDetail(DetailView):
    context_object_name = 'musician'
    model = Musician
    template_name = 'CLSBV/musician_detail.html'

class AlbumDetail(DetailView):
    context_object_name = "album"
    model = Album
    template_name = 'CLSBV/album_detail.html'

    ## why this this necessary for Album details
    ## and not for MusicianDetails
    ## because Album detail has more than 1 key
    ## 1 primary key
    ## 1 foreign key
    ## so we dont know which key based we sort
    ## so we says that in the get_queryset methods

    def get_queryset(self):
        return Album.objects.order_by('-release_date')






## we now we create a Create View for Alnum and the musician


class CreateMusician(CreateView):
    model = Musician
    ## you need to provide the fields
    fields = ('first_name','last_name','instrument')

class CraeteAlbum(CreateView):

    ## of course form class when you do the date input
    form_class = AlbumForm
    model = Album
    ## we will do that using form
    ## can can also intregate form with the Create View
    


class UpdateMusician(UpdateView):
    ## always put the fields in the first

    fields = ('first_name','last_name')
    model = Musician
    


class UpdateAlbum(UpdateView):
    form_class = AlbumForm
    model = Album


class DeleteMusician(DeleteView):
    model = Musician
    success_url = reverse_lazy("CLSBV:view_list")

class DeleteAlbum(DeleteView):
    model = Album
    success_url = reverse_lazy("CLSBV:view_list")

