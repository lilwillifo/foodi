from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)

class Food(models.Model):
        # import code; code.interact(local=dict(globals(), **locals()))
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    serving_qty = models.IntegerField()
    serving_unit = models.IntegerField()
    calories = models.IntegerField()
    total_fat = models.IntegerField()
    sat_fat = models.IntegerField()
    cholesterol = models.IntegerField()
    sodium = models.IntegerField()
    carbs = models.IntegerField()
    fiber = models.IntegerField()
    sugar = models.IntegerField()
    protein = models.IntegerField()
    # self.name = food_data['food_name'].capitalize
    # self.img = food_data['photo']
    # self.serving_qty = food_data['serving_qty']
    # self.serving_unit = food_data['serving_unit']
    # self.calories = round(food_data['nf_calories'])
    # self.total_fat = round(food_data['nf_total_fat'], 1)
    # self.sat_fat = round(food_data['nf_saturated_fat'], 1)
    # self.cholesterol = round(food_data['nf_cholesterol'], 1)
    # self.sodium = round(food_data['nf_sodium'], 1)
    # self.carbs = round(food_data['nf_total_carbohydrate'])
    # self.fiber = round(food_data['nf_dietary_fiber'], 1)
    # self.sugar = round(food_data['nf_sugars'], 1)
    # self.protein = round(food_data['nf_protein'], 1)
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
