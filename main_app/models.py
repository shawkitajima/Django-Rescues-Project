from django.db import models
from django.urls import reverse
# Create your models here.

class Adopter(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return f'{self.name} has an id of {self.id}'
    
    def get_absolute_url(self):
        return reverse('adopters_detail', kwargs={'pk': self.id})


class Rescue(models.Model):
    name = models.CharField(max_length=100)
    animal = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    adopters = models.ManyToManyField(Adopter)

    def __str__(self):
        return f'{self.name} is a {self.animal} with an id of {self.id}'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'rescue_id': self.id})


class Gift(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    rescue = models.ForeignKey(Rescue, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} was provided on {self.date} to {self.rescue.name}'

    class Meta:
        ordering=['-date']

class Photo(models.Model):
    url = models.CharField(max_length=100)
    rescue = models.ForeignKey(Rescue, on_delete=models.CASCADE)

    def __str__(self):
        return f'the url is {self.url}'