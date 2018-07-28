from django.core.management.base import BaseCommand, CommandError
from foodi.models import Profile, Food, Diary
from foodi.food_service import FoodService
from django.contrib.auth.models import User
from decouple import config
from faker import Faker
import requests
import random
from random import randint
from datetime import datetime
from IPython import embed

class Command(BaseCommand):
    help='Seeding the database'
    fake = Faker()

    def _create_foods(self):
        foods = ['apple', 'banana', 'carrot', 'donut', 'eggs', 'fruitcake',
                 'hot dog', 'ice cream', 'jerky', 'kit kat', 'lemonade', 'mac and cheese', 'nuts',
                 'rice', 'snickers', 'tacos', 'veal', 'steak']
        for food in foods:
            url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
            headers = {'x-app-id': config('NIX_APP_ID'),
                       'x-app-key': config('NIX_APP_KEY'),
                       'x-remote-user-id': '0'}
            payload = {'query': food}

            response = requests.post(url, headers=headers, data=payload)
            search_result = response.json()
            if 'foods' in search_result:
                raw_food = FoodService(search_result['foods'][0])
                try:
                    food = Food.objects.get(name = raw_food.name)
                except Food.DoesNotExist:
                    food  = Food(name = raw_food.name,
                                   img = raw_food.img['thumb'],
                                   serving_qty = raw_food.serving_qty,
                                   serving_unit = raw_food.serving_unit,
                                   calories = raw_food.calories,
                                   total_fat = raw_food.total_fat,
                                   sat_fat = raw_food.sat_fat,
                                   cholesterol = raw_food.cholesterol,
                                   sodium = raw_food.sodium,
                                   carbs = raw_food.carbs,
                                   fiber = raw_food.fiber,
                                   sugar = raw_food.sugar,
                                   protein = raw_food.protein)
                    food.save()

    def _create_diaries(self):
        users = User.objects.all()
        for user in users:
            for _ in range(1,100):
                food = Food.objects.order_by('?').first()
                year = random.randint(2017, 2018)
                month = random.randint(1, 12)
                day = random.randint(1, 28)
                date = f"{year}-{month}-{day}"
                Diary.objects.create(food=food, user=user.profile, servings=randint(1,5), date_eaten=date )


    def handle(self, *args, **options):
        self._create_foods()
        self._create_diaries()
