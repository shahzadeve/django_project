from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name
    

    
class Watchlist(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    storyline = models.CharField(max_length=100, blank=True, default='')
    avg_rating = models.FloatField(default=0)
    number_rating = models.IntegerField(default=0 )
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name='watchlist')
    active  = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', null=True)
    rating = models.PositiveIntegerField(validators= [
        MinValueValidator(1),
        MaxValueValidator(5)
    ])
    description = models.CharField(max_length=200)
    watchlist = models.ForeignKey(Watchlist, on_delete=models.CASCADE, related_name='reviews')
    update = models.DateTimeField(auto_now=True) 
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True) 

    def __str__(self):
        return str(self.rating)
