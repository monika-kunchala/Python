Menu = {
    "summer_collection": {
            "items": {
                "T-shirts": 2,
                "pants": 2,
                "accessories": 1,
            },
            "cost": 3500
        },

        "winter_collection": {
            "items": {
                "hoddies": 2,
                "pants": 2,
                "accessories": 1,
            },
            "cost": 4500
        },

        "spring_collection": {
            "items": {
                "T-shirts": 2,
                "pants": 2,
                "accessories": 1,
            },
            "cost": 3000
        }
    }


profit = 0

resources = {
    "T-shirts" : 10,
    "pants" : 10,
    "hoddies": 10,
    "accessories" : 10,

}
def is_resoureces_sufficient(order_items):
      for item in order_items:
            if order_items[item] > resources[item]:
                  print(f"sorry there is not enough {item}.")
                  return False
            
      return True

def process_money():
      print("please enter money")
      total = int(input("how many 100rs? :")) *100
      total += int(input("how many 500rs?:")) *500
      total += int(input("how many 1000rs? : ")) *1000
      return total

def is_trasacation_successfull(money_received,order_cost):
      if money_received >= order_cost:
            change = round(money_received - order_cost,2)
            global profit
            profit += order_cost
            return True
      else:
            print("sorry that not enough money, money refunded")
            return False
      
def make_order(collection_name, order_items):
      for item in order_items:
            resources[item] -= order_items[item]
      print(f"here is ur {collection_name} . thank you for visting us")

is_on = True

while is_on:
        collection_order  = input('what would like to have to order (summer_collection/winter_collection/spring_collection)? :')
        if collection_order == "off":
            is_on = False
        elif collection_order == "report":
              print(f"T-shirts : {resources['T-shirts']} pics")
              print(f"pants : {resources['pants']}pics")
              print(f"hoddies: {resources['hoddies']}pics")
              print(f"accessories : {resources['accessories']}pics")
              print(f"money ${profit}")
        else:
             order = Menu[collection_order]
             if is_resoureces_sufficient(order['items']):
                   payment = process_money()
                   if is_trasacation_successfull(payment, order['cost']):
                         make_order(collection_order, order['items'])
