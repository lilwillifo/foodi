from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Food(models.Model):
        # import code; code.interact(local=dict(globals(), **locals()))
    name = models.CharField(max_length=100, unique=True)
    img = models.CharField(max_length=1000)
    serving_qty = models.IntegerField()
    serving_unit = models.CharField(max_length=500)
    calories = models.IntegerField()
    total_fat = models.FloatField()
    sat_fat = models.FloatField()
    cholesterol = models.FloatField()
    sodium = models.FloatField()
    carbs = models.FloatField()
    fiber = models.FloatField()
    sugar = models.FloatField()
    protein = models.FloatField()
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

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Diary(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    date_eaten = models.DateField()
    servings = models.FloatField()
