from django.db import models

# Create your models here.
class Building(models.Model):
    name = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=10)
    # store reference to svg file here?
    
    def __str__(self):
        return self.name

class Floor(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    number = models.IntegerField(default=-1)
    # store reference to svg file here?
    
    def __str__(self):
        return self.number

class Room(models.Model):
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)

    def __str__(self):
        return self.number