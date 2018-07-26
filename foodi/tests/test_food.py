from django.test import TestCase
from foodi.models import Food

class FoodTestCase(TestCase):
    def setUp(self):
        Food.objects.create(name="candy",
                            img='',
                            serving_qty = 1,
                            serving_unit = 'something',
                            calories = 200,
                            total_fat = 5,
                            sat_fat = 5,
                            cholesterol = 5,
                            sodium = 5,
                            carbs = 5,
                            fiber = 5,
                            sugar = 5,
                            protein = 5,)

    def test_food_has_attributes(self):
        food = Food.objects.get(name="candy")
        self.assertEqual(food.serving_qty, 1)
        self.assertEqual(food.total_fat, 5)
        self.assertEqual(food.sat_fat, 5)
        self.assertEqual(food.cholesterol, 5)
        self.assertEqual(food.sodium, 5)
        self.assertEqual(food.carbs, 5)
        self.assertEqual(food.fiber, 5)
        self.assertEqual(food.sugar, 5)
        self.assertEqual(food.protein, 5)

    def test_it_stores_percent_daily_values(self):
        food = Food.objects.get(name="candy")
        self.assertEqual(food.calorieIntake, 2000)
        self.assertEqual(food.dailyValueTotalFat,65)
        self.assertEqual(food.dailyValueSatFat,20)
        self.assertEqual(food.dailyValueCholesterol,300)
        self.assertEqual(food.dailyValueSodium,2400)
        self.assertEqual(food.dailyValueCarb,300)
        self.assertEqual(food.dailyValueFiber,25)
        self.assertEqual(food.dailyValueCalcium,1300)

    def test_it_can_find_percent_daily_value(self):
        food = Food.objects.get(name="candy")
        self.assertEqual(food.fat_percent(), 7.69)
        self.assertEqual(food.sat_fat_percent(), 25.0)
        self.assertEqual(food.cholesterol_percent(), 1.67)
        self.assertEqual(food.sodium_percent(), 0.21)
        self.assertEqual(food.carb_percent(), 1.67)
        self.assertEqual(food.fiber_percent(), 20.0)
