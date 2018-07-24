from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)

class Food(models.Model):
        # import code; code.interact(local=dict(globals(), **locals()))
    name = models.CharField(max_length=100, unique=True)
    img = models.CharField(max_length=1000)
    serving_qty = models.IntegerField()
    serving_unit = models.CharField(max_length=500)
    calories = models.IntegerField()
    total_fat = models.IntegerField()
    sat_fat = models.IntegerField()
    cholesterol = models.IntegerField()
    sodium = models.IntegerField()
    carbs = models.IntegerField()
    fiber = models.IntegerField()
    sugar = models.IntegerField()
    protein = models.IntegerField()
    calorieIntake = 2000
    dailyValueTotalFat = 65
    dailyValueSatFat = 20
    dailyValueCholesterol = 300
    dailyValueSodium = 2400
    dailyValueCarb = 300
    dailyValueFiber = 25
    dailyValueCalcium = 1300

    users = models.ManyToManyField(User, through='Diary')

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

class Diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    date_eaten = models.DateField()
