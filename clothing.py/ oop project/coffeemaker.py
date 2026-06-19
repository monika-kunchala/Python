class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 500,
            "milk" : 300,
            "coffee" : 250,
        }

    def report(self):
        print(f"water: {self.resources['water']}ml")
        print(f"milk: {self.resources['milk']}ml")
        print(f"coffee: {self.resources['coffee']}ml")


    def is_resources_sufficient(self, drink):
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"sorry there is not enough {item}")
                can_make = False
        return can_make


    def make_coffee(self, order): 
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item] 
        print(f"here is your {order.name} enjoy") 


"""maker = CoffeeMaker()
maker.report()"""
