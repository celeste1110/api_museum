from django.db import models

# Create your models here.

class Artist(models.Model):
    
    mame =  models.CharField(max_length = 200)
    biography = models.TextField(max_length = 2000)
    birth_date = models.DateField()
    country = models.CharField(max_length = 200)
    image = models.ImageField(upload_to="artists",null=True)
    
class Medium(models.Model):
    
    description =  models.CharField(max_length = 200)
    status = models.BooleanField()

class Museum(models.Model):
    
    mame =  models.CharField(max_length = 200)
    description =  models.CharField(max_length = 200)
    city =  models.CharField(max_length = 200)
    country =  models.CharField(max_length = 200)
    address =  models.CharField(max_length = 200)
    lat =  models.FloatField(null=True)
    lon =  models.FloatField(null=True)
    image = models.ImageField(upload_to="museums",null=True)

class CulturalProperty(models.Model):
    
    mame =  models.CharField(max_length = 200)
    description =  models.CharField(max_length = 200)
    city =  models.CharField(max_length = 200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    medium = models.ForeignKey(Medium, on_delete=models.CASCADE)
    museum = models.ForeignKey(Museum, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="properts",null=True)
    
    
    
   
    
    
    
    

