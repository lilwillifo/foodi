from django.test import TestCase
from foodi.models import Diary, Food, User, Profile

class DiaryTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="Katelyn")
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

    def test_diary_has_attributes(self):
        user = User.objects.get(username="Katelyn").profile
        food = Food.objects.get(name="candy")
        diary = Diary.objects.create(food=food, user=user, servings=2, date_eaten='2018-08-27')
        self.assertEqual(diary.food, food)
        self.assertEqual(diary.user, user)
        self.assertEqual(diary.servings, 2)
        self.assertEqual(diary.date_eaten, '2018-08-27')
