"""User models."""
#Django 
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Country(models.Model):
    IdCountry = models.AutoField(primary_key=True)
    NamCountry = models.CharField(max_length=35, blank=True)
    
    def __str__(self):
        return self.NamCountry
    
    
class House(models.Model):
    IdHouse = models.AutoField(primary_key=True)
    NamHouse = models.CharField(max_length=35, blank=True)

class Patronus(models.Model):
    IdPatronus = models.AutoField(primary_key=True)
    NamPatronus = models.CharField(max_length=35, blank=True)

class  Profile(models.Model):
    """Profile model
        Proxy model that extends the base data with
        other information
    """
    NamUser = models.OneToOneField(User, on_delete=models.CASCADE)       
    
    FirstNamUser = models.CharField(max_length=35, blank=True)
    LastNamUser = models.CharField(max_length=35, blank=True)
    BirthUser = models.DateTimeField(auto_now=True)
    BiographyUser = models.TextField(blank=True)
    CountryUser = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    HouseUser = models.ForeignKey(House, on_delete=models.CASCADE, null=True)
    PatronusUser = models.ForeignKey(Patronus, on_delete=models.CASCADE, null=True)
    
    CreateUser = models.DateTimeField(auto_now_add=True)
    ModifiedUser = models.DateTimeField(auto_now=True)
    
    picture = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
        )
    
    def __str__(self):
        return self.user.username