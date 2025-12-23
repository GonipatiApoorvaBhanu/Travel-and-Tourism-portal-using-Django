from django.db import models

# Create your models here.



class Tour(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name

class Bus(models.Model):
    name = models.CharField(max_length=100)
    seats = models.IntegerField(default=40)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
