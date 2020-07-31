from django.db import models

class Musician(models.Model):
    first_name  = models.CharField(max_length=150)
    last_name   = models.CharField(max_length=150)
    instrument  = models.CharField(max_length=150)


    def __str__(self):
        return self.first_name + " " + self.last_name


class Album(models.Model):
    artist       = models.ForeignKey(Musician,on_delete=models.CASCADE)
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
