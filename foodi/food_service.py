class FoodService():
    def __init__(self, food_data):
        # import code; code.interact(local=dict(globals(), **locals()))
        self.name = food_data['food_name'].capitalize()
        self.img = food_data['photo']
        self.serving_qty = food_data['serving_qty']
        self.serving_unit = food_data['serving_unit']
        self.calories = round(food_data['nf_calories'])
        self.total_fat = round(food_data['nf_total_fat'], 1)
        self.sat_fat = round(food_data['nf_saturated_fat'], 1)
        self.cholesterol = round(food_data['nf_cholesterol'], 1)
        self.sodium = round(food_data['nf_sodium'], 1)
        self.carbs = round(food_data['nf_total_carbohydrate'])
        self.fiber = round(food_data['nf_dietary_fiber'], 1)
        self.sugar = round(food_data['nf_sugars'], 1)
        self.protein = round(food_data['nf_protein'], 1)
