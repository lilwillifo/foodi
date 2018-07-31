from django.test import TestCase
from foodi.models import Profile, User, Food, Diary
from IPython import embed

class ProfileTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="example")

    def test_profile_has_attributes(self):
        user = User.objects.get(username="example")
        profile = user.profile
        self.assertEqual(profile.user, user)
        self.assertFalse(profile.foods.all().exists() )

    def test_it_can_have_many_foods(self):
        user = User.objects.get(username="example")
        food = Food.objects.create(name="candy")
        diary = Diary.objects.create(user=user.profile, food=food, servings=2, date_eaten="2018-02-15")
        self.assertEqual(user.profile.foods.all().first(), food)

    def test_it_returns_top_5_foods_for_user(self):
        user = User.objects.get(username="example")
        candy = Food.objects.create(name="candy")
        popcorn = Food.objects.create(name="popcorn")
        tea = Food.objects.create(name="tea")
        coffee = Food.objects.create(name="coffee")
        cereal = Food.objects.create(name="cereal")
        bread = Food.objects.create(name="bread")
        diary = Diary.objects.create(user=user.profile, food=candy, servings=10, date_eaten="2018-02-15")
        diary = Diary.objects.create(user=user.profile, food=popcorn, servings=1, date_eaten="2018-01-15")
        diary = Diary.objects.create(user=user.profile, food=tea, servings=2, date_eaten="2018-02-20")
        diary = Diary.objects.create(user=user.profile, food=coffee, servings=3, date_eaten="2014-02-22")
        diary = Diary.objects.create(user=user.profile, food=cereal, servings=3, date_eaten="2018-08-15")
        diary = Diary.objects.create(user=user.profile, food=bread, servings=2, date_eaten="2018-08-11")
        self.assertEqual(len(user.profile.top_5_foods()), 5)
        self.assertEqual(user.profile.top_5_foods()[0], ('candy', 10.0))
        self.assertEqual(user.profile.top_5_foods()[4], ('bread', 2.0))

    def test_it_does_notreturn_top_5_foods_for_user_if_no_foods(self):
        user = User.objects.get(username="example")
        self.assertEqual(len(user.profile.top_5_foods()), 0)
