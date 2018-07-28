from django.core.management.base import BaseCommand
from foodi.models import Profile, Food, Diary
from django.contrib.auth.models import User
from faker import Faker

class Command(BaseCommand):
    help='Seeding the database'

    def _create_foods(self):
        for _ in range(100):
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

    def handle(self, *args, **options):
        self._create_foods()
