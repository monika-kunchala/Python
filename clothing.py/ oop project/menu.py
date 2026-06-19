class MENUItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk" : milk,
            "coffee": coffee,
        }

class MENU:
    def __init__(self):
        self.menu = [
            MENUItem(name = 'latte', water = 100, milk = 150, coffee = 24, cost = 25),
            MENUItem(name = 'cappuchino', water = 50, milk= 100, coffee= 50, cost= 30),
            MENUItem(name = 'esprsso', water = 150, milk= 20, coffee= 60, cost = 35)
        ]
    
    
    def get_item(self):
        options = " "
        for item in self.menu:
            options += f"{item.name}/"
        return options
    

    def find_drink(self, order_name):
        for item in self.menu:
            if item.name  == order_name:
                return item
        print("sorry that item is  not avilable")


"""menu = MENU()
print(menu.get_item())
coffee = menu.find_drink('latte')
print(coffee.name)"""
