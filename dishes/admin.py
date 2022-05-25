from ssl import DefaultVerifyPaths
from django.contrib import admin
from django.db.models import Count
from .models import User, Dish, Ingredient
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super(UserAdmin, self).get_queryset(request)
        return qs.annotate(dishes_count=Count('dishes'))

    def dishes_count(self, inst):
        return inst.dishes_count

    list_display = ['first_name', 'last_name', 'dishes_count']
    fieldsets = (
        ('User info', {'fields': ('first_name', 'last_name')}),
        ('Dishes', {'fields': ('dishes',)})
    )


@admin.register(Dish)
class DishesAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(DishesAdmin, self).get_queryset(request)
        return qs.annotate(ingredients_count=Count('ingredients_id'))

    def ingredients_count(self, inst):
        return inst.ingredients_count

    list_display = ['dish_name', 'calories', 'ingredients_count']
    fieldsets = (
        (None, {'fields': ('dish_name',)}),
        ('Nutrimental info', {'fields': ('calories',)}),
        ('Ingredients', {'fields': ('ingredients_id',)})
    )


@admin.register(Ingredient)
class IngredientsAdmin(admin.ModelAdmin):
    list_display = ('ingredient', 'calories')
    fieldsets = (
        (None, {'fields': ('ingredient',)}),
        ('Nutrimental info', {'fields': ('calories',)})
    )