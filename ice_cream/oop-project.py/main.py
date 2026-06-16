from Menu import Menu
from icecream import IceCreamMaker
from money_maker import MoneyMachine

money_machine = MoneyMachine()
icecream_maker = IceCreamMaker()
menu = Menu()


is_on = True


while is_on:
    options = menu.get_item()
    choice = input(f"what would u like ? ({options})")
    if choice == "off":
        is_on = False
    elif choice == 'report':
        icecream_maker.report()
        money_machine.report()
    else:
        icecream = menu.find_icecream(choice)
        if icecream_maker.is_resource_sufficient(icecream) and money_machine.make_payment(icecream.cost):
                print(icecream_maker.make_icecream(icecream))

