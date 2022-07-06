from dishes.models import Food
import csv

def run():
    with open('./Data/food.csv') as file:
        reader = csv.reader(file)
        next(reader) #skip header

        Food.objects.all().delete()

        for row in reader:
            food = Food(fcd_id = row[0],
                        description = row[1])

            food.save