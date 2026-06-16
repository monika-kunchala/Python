class IceCreamMaker:
    def __init__(self):
        self.resources = {
            "water": 500,
            "venilla_syrup" : 200,
            "chocolate_syrup": 200,
            "ice": 300,
        }

    def report(self):
        print(f"water: {self.resources['water']}ml")
        print(f"venilla_syrup: {self.resources['venilla_syrup']}ml")
        print(f"chocolate_syrup: {self.resources['chocolate_syrup']}ml")
        print(f"ice: {self.resources['ice']}ml")


    def is_resource_sufficient(self, icecream):
        can_make = True
        for item in icecream.ingredients:
            if icecream.ingredients[item] > self.resources[item]:
                print(f"sorry thats not enough {item} .")
                can_make = False
        return can_make
    
    def make_icecream(self, order):
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"here is your {order.name} enjoy!")


"""maker = IceCreamMaker()
maker.report()"""