from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum
from collections import Counter


class Food(models.Model):
        # import code; code.interact(local=dict(globals(), **locals()))
    name = models.CharField(max_length=100, unique=True)
    img = models.CharField(max_length=1000, null=True, blank=True)
    serving_qty = models.IntegerField(null=True, blank=True)
    serving_unit = models.CharField(max_length=500, null=True, blank=True)
    calories = models.IntegerField(null=True, blank=True)
    total_fat = models.FloatField(null=True, blank=True)
    sat_fat = models.FloatField(null=True, blank=True)
    cholesterol = models.FloatField(null=True, blank=True)
    sodium = models.FloatField(null=True, blank=True)
    carbs = models.FloatField(null=True, blank=True)
    fiber = models.FloatField(null=True, blank=True)
    sugar = models.FloatField(null=True, blank=True)
    protein = models.FloatField(null=True, blank=True)
    calorieIntake = 2000
    dailyValueTotalFat = 65
    dailyValueSatFat = 20
    dailyValueCholesterol = 300
    dailyValueSodium = 2400
    dailyValueCarb = 300
    dailyValueFiber = 25
    dailyValueCalcium = 1300

    def __str__(self):
        return self.name

    def fat_percent(self):
        return round(self.total_fat / self.dailyValueTotalFat  * 100, 2)

    def sat_fat_percent(self):
        return round(self.sat_fat / self.dailyValueSatFat  * 100, 2)

    def cholesterol_percent(self):
        return round(self.cholesterol / self.dailyValueCholesterol  * 100, 2)

    def sodium_percent(self):
        return round(self.sodium / self.dailyValueSodium  * 100, 2)

    def carb_percent(self):
        return round(self.carbs / self.dailyValueCarb  * 100, 2)

    def fiber_percent(self):
        return round(self.fiber / self.dailyValueFiber  * 100, 2)

        class Meta:
            ordering = ('id',)

# class adds on additional functionality to built in user table.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foods = models.ManyToManyField(Food, through='Diary', related_name='users')
    def top_5_foods(self):
        food_count = dict()
        for food in self.foods.all():
            food_count[food.name] = self.diaries.filter(food=food).aggregate(total_servings=Sum('servings'))['total_servings']
        top_5 = Counter(food_count).most_common()[:5]
        return top_5

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Diary(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='diaries')
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='diaries')
    date_eaten = models.DateField()
    servings = models.FloatField()
    class Meta:
        ordering = ['date_eaten']
