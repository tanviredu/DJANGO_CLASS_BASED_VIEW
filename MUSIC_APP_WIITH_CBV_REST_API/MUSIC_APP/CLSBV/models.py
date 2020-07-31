from django.db import models
from django.urls import reverse,reverse_lazy
class Musician(models.Model):
    first_name  = models.CharField(max_length=150)
    last_name   = models.CharField(max_length=150)
    instrument  = models.CharField(max_length=150)


    def __str__(self):
        return self.first_name + " " + self.last_name


    ## after saving where the page go

    def get_absolute_url(self):
        ## the kwargs have to be used 
        ## for addtional parameter
        #return reverse("CLSBV:index", kwargs={"pk": self.pk})
        #return reverse('CLSBV:index')


        ## we pass the detail url so we need
        ## to give the pk too so we and kwargs
        return reverse("CLSBV:mdetail",kwargs={'pk':self.pk})
    

#####

    #   REMEMBER WE CAN ACCESS ANY artise in th album with the 
    #   keywornd album1.artist.first_name
    #            album1.artist.last_name   etc

    ## for reverse match we can use the related_name
    # musician.album_list.name
    # musician.album_list.release_date
    # etc so we can call thge album from the musician list too



#####


class Album(models.Model):
    artist       = models.ForeignKey(Musician,on_delete=models.CASCADE,related_name='album_list')
    name         = models.CharField(max_length=150)
    release_date = models.DateField()

    rating = (
        (1,'very bad'),
        (2,'bad'),
        (3,'good'),
        (4,'very good'),
        (5,'Excelent!'),
    )  
    num_starts = models.IntegerField(choices=rating)


    def __str__(self):
        return "Album Name : {} \n Artist Name {}".format(self.name,self.artist)


    def get_absolute_url(self):
        return reverse("CLSBV:adetail", kwargs={"pk": self.pk})
    