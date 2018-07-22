class FoodService():
    def __init__(self, food_data):
        # import code; code.interact(local=dict(globals(), **locals()))
        self.name = food_data['food_name'].capitalize
        self.serving_qty = food_data['serving_qty']
        self.calories = round(food_data['nf_calories'])
        self.total_fat = round(food_data['nf_total_fat'], 1)
        self.sat_fat = round(food_data['nf_saturated_fat'], 1)
        self.cholesterol = round(food_data['nf_cholesterol'], 1)
        self.sodium = round(food_data['nf_sodium'], 1)
        self.carbs = round(food_data['nf_total_carbohydrate'])
        self.fiber = round(food_data['nf_dietary_fiber'], 1)
        self.sugar = round(food_data['nf_sugars'], 1)
        self.protein = round(food_data['nf_protein'], 1)
        self.calorieIntake = 2000
        self.dailyValueTotalFat = 65
        self.dailyValueSatFat = 20
        self.dailyValueCholesterol = 300
        self.dailyValueSodium = 2400
        self.dailyValuePotassium = 3500
        self.dailyValuePotassium_2018 = 4700
        self.dailyValueCarb = 300
        self.dailyValueFiber = 25
        self.dailyValueCalcium = 1300
        self.dailyValueIron = 18
        self.dailyValueVitaminD = 20
        self.dailyValueAddedSugar = 50

    def fat_percent(self):
        return round(self.total_fat / self.dailyValueTotalFat, 2) * 100

    def sat_fat_percent(self):
        return round(self.sat_fat / self.dailyValueSatFat, 2) * 100

    def cholesterol_percent(self):
        return round(self.cholesterol / self.dailyValueCholesterol, 2) * 100

    def sodium_percent(self):
        return round(self.sodium / self.dailyValueSodium, 2) * 100

    def carb_percent(self):
        return round(self.carbs / self.dailyValueCarb, 2) * 100

    def fiber_percent(self):
        return round(self.fiber / self.dailyValueFiber, 2) * 100
