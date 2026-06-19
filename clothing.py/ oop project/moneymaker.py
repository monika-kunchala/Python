class MoneyMAchine:

    CURRENCY = "$"

    COIN_VALUES = {
        "1rs" : 1,
        "5rs" : 5,
        "10rs": 10

    }
    

    def __init__(self):
        self.profit = 0
        self.money_received = 0


    def report(self):
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        print("please insert coins")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"how many {coin}?:")) * self.COIN_VALUES[coin]
        return self.money_received
    
    def make_payment(self,cost):
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"here is {self.CURRENCY}{change} in change")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("sorry thats not enough money. money refuded")
            self.money_received = 0
            return False
        

"""machine = MoneyMAchine()
machine.report()
machine.make_payment(30)
machine.report()   """    
