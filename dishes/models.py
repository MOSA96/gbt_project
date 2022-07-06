from django.db import models

# Create your models here.


class Ingredient(models.Model):
    ingredient = models.CharField(max_length=50)
    calories = models.IntegerField()



class Dish(models.Model):
    dish_name = models.CharField(max_length=50)
    calories = models.IntegerField()
    quantity = models.IntegerField()
    ingredients_id = models.ManyToManyField(Ingredient) 


class Food(models.Model):
    fcd_id = models.IntegerField()
    description = models.TextField()


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dishes = models.ManyToManyField(Dish)
    def __str__(self):
        return self.first_name
