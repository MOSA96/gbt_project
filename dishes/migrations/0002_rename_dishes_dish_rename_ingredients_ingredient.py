# Generated by Django 4.0.4 on 2022-05-24 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Dishes',
            new_name='Dish',
        ),
        migrations.RenameModel(
            old_name='Ingredients',
            new_name='Ingredient',
        ),
    ]
