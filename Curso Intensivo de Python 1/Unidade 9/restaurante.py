class Restaurant0:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Restaurante: {self.restaurant_name} nos somos uma cozinha{self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"O restaurante {self.restaurant_name} está aberto.")
