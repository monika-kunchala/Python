class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "1rs": 1,
        "5rs": 5,
        "10rs": 10
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        print("please insert coins")
        for coins in self.COIN_VALUES:
            self.money_received += int(input(f"how many {coins}?:")) * self.COIN_VALUES[coins] 
        return self.money_received

    def make_payment(self, cost):
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost,2)
            print(f"here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print('sorry that not enough money. money refunded')
            self.money_received = 0
            return False
        
"""machine = MoneyMachine()
machine.report()
machine.make_payment(15)
machine.report()"""