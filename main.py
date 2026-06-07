MENU = {
    "venila" : {
        "ingredients" :{
            "water": 100,
            "venila_syrup" : 20,
            "ice" : 5,
        },

        "cost": 15,
    },

    "chocolate" : {
        "ingredients": {
            "water": 200,
            "chocolate_syrup": 20,
            "ice": 10,
        },

        "cost": 20,
    },

    "mix" : {
        "ingredients": {
            "water" : 200,
            "venila_syrup": 20,
            "chocolate_syrup" : 20,
            "ice": 15,
        },

        "cost": 25
    }
}

profit = 0
  
resources  = {
    "water": 300,
    "venila_syrup" : 40,
    "chocolate_syrup": 40,
    "ice" : 30

}

def  is_resources_sufficient(order_ingrdients):
    """if we have or havent have sufficiet resources"""
    for item in order_ingrdients:
        if order_ingrdients[item] > resources[item]:
            print(f"sorry there is not enough {item}")
            return False
    return True

def process_coins():
    "return the total calculated from coins"
    print("please insert coins.")
    total = int(input("how many 1rs?: ")) *1
    total += int(input("how many 5rs?:")) *5
    total += int(input("how many 10rs?:")) *10
    return total 

def is_transaction_successful(money_received, ice_cream_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= ice_cream_cost:
        change = round(money_received - ice_cream_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += ice_cream_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_ice_cream(ice_cream, order_ingredients):
    """deduct the required ingredients from the resoureces"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your {ice_cream} . enjoy")
    
is_on = True

while is_on:
    choice = input("what would u like ? (venila/chocolate/mix) :")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources ['water']}  ml")
        print(f"venila_syrup :{resources ['venila_syrup']} ml")
        print(f"chocolate_syrup:{resources ['chocolate_syrup']} ml")
        print(f"ice : {resources ['ice']}  cubs")
        print(f"Money $ {profit}")
    else:
        ice_cream = MENU[choice]
        if is_resources_sufficient(ice_cream['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, ice_cream['cost']):
                make_ice_cream(choice, ice_cream['ingredients'])
