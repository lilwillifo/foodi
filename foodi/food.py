class FoodService():
    def __init__(self, food_data):
        # import code; code.interact(local=dict(globals(), **locals()))
        self.name = food_data['food_name'].capitalize
        self.serving_qty = food_data['serving_qty']
