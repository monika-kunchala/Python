class MenuItem:
    def __init__(self, name, water, ice, cost, venilla_syrup = 0, chocolate_syrup = 0):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "ice": ice,
            "venilla_syrup": venilla_syrup,
            "chocolate_syrup": chocolate_syrup 

        }

class Menu():
    def __init__(self):
        self.menu = [
            MenuItem(name='venilla_icecream', water= 100, venilla_syrup=20, ice=10, cost=15),
            MenuItem(name='chocolate_icecream', water=100, chocolate_syrup=20, ice= 10, cost=20),
            MenuItem(name='mix', water=100, venilla_syrup=10, chocolate_syrup=10, ice =5, cost=25)
        ]
    
    def get_item(self):
        options = " "
        for item in self.menu:
            options += f"{item.name}/"
        return options


    def find_icecream(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        print("sorry that item is not available .")



"""menu = Menu()
print(menu.get_item())
icecream = menu.find_icecream('mix')
print(icecream.name)"""
