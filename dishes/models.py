from django.db import models

# Create your models here.


class Ingredients(models.Model):
    ingredient = models.CharField(max_length=50)
    calories = models.IntegerField()



class Dishes(models.Model):
    dish_name = models.CharField(max_length=50)
    calories = models.IntegerField()
    quantity = models.IntegerField()
    ingredients_id = models.ManyToManyField(Ingredients) 


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dishes = models.ManyToManyField(Dishes)
    def __str__(self):
        return self.first_name