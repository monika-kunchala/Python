rom logo import logo
from logo import vs 
from sales import data
import random


def format_data(account):
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_descr} from {account_country}"

def check_answer(user_guess, a_sales, b_sales):
    if a_sales > b_sales:
        return user_guess == 'a'
    else:
        return user_guess == 'b'



print(logo)
score = 0
game_shoule_continue = True

while game_shoule_continue:
    account_a = random.choice(data)
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)


    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"compare A: {format_data(account_a)}.")
    print(vs)
    print(f"compare B: {format_data(account_b)}.")

    guess = input("who has more sales ? Type 'A' or 'B':").lower()

    a_sales_count = account_a['sales_count']
    b_sales_count = account_b['sales_count']
    is_correct = check_answer(guess, a_sales_count,b_sales_count)

    if is_correct:
        score += 1
        print(f"your right. current score is {score}")
    else:
        print(f"sorry thats wrong .current score is {score}")
        game_shoule_continue = False
