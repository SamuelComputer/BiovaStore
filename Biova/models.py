from django.db import models
from datetime import datetime




class Product(models.Model):
    name = models.CharField(max_length= 20)
    picture = models.ImageField()
    price = models.IntegerField()
    description = models.TextField(default= "type details here")
    

    def __str__(self):
        return f"{self.name} | {self.price}"



class Categorie(models.Model):
    name = models.CharField(max_length= 20)
    picture = models.ImageField()
    description = models.TextField()
    
    def __str__(self):
        return f"{self.name} | {self.description}"




class Review(models.Model):
    name = models.CharField(max_length= 20)
    picture = models.ImageField()
    review = models.TextField()

    
    def __str__(self):
        return f"{self.name} | {self.review}"




class Blog(models.Model):
    name = models.CharField(max_length= 20)
    picture = models.ImageField()
    description = models.TextField()
    date = models.DateTimeField( default= datetime.now)

    
    def __str__(self):
        return f"{self.name} | {self.date}"