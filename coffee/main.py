Memu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "costs" : 1.5,
    },

    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "costs" : 20.0,
    },

    "cappuccino": {
        "ingredients": {
            "water" : 250,
            "milk" : 100,
            "coffee": 24,        
        },
        "costs": 15.0,
    }
    
}
profit  = 0

resources = {
    "water": 300,
    "milk" : 200,
    "coffee": 100,
}

def is_resources_sufficient(order_ingredients):
    """if we do or dont have sufficient resources """
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"sorry there is not enough {item}.")
            return False
    return True

def process_coin():
    """REturn the total calculated from coins inserted"""
    print("please insert coins.")
    total  = int(input("how many 50 p?: ")) *0.50
    total  += int(input("how many 1rs?: ")) *1
    total  += int(input("how many 5rs?: ")) *5
    total  += int(input("how many 10rs?: ")) *10
    return total

def is_trasacation_successful(money_received, drink_cost):
    """REturn true when money is accepted , or false if money is ineffeicient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry thats not enough money .money refunded")
        return False


def make_coffe(drink_name, order_ingredients):
    """deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")
              
    
is_on = True

while is_on:
    choice = input("what would u like? (espresso/latte/cappuccino) : ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk : {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money: ${profit}")
    else:
        drink = Memu[choice]
        if is_resources_sufficient(drink['ingredients']):
            payment = process_coin()
            if is_trasacation_successful(payment, drink['costs']):
                make_coffe(choice, drink["ingredients"])
