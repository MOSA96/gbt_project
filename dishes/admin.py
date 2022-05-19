from django.contrib import admin
from .models import User, Dishes, Ingredients
# Register your models here.

admin.site.register(User)
admin.site.register(Dishes)
admin.site.register(Ingredients)