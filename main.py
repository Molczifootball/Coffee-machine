from machine import *
from coins import *
to_do = "x"
def report():
    print(machine)
def check_machine(coffee):
    if machine["Water"] - coffee["Water"] < 0:
        print("Not enough water.")
        return 0
    elif machine["Milk"] - coffee["Milk"] < 0:
        print("Not enough milk.")
        return 0
    elif machine["Coffee"] - coffee["Coffee"] < 0:
        print("Not enough coffee.")
        return 0
    else:
        machine["Water"] -= coffee["Water"]
        machine["Milk"] -= coffee["Milk"]
        machine["Coffee"] -= coffee["Coffee"]
        return 1

def check_money(coffee):
    price = coffee["Price"]
    print("Proceeding...")
    print(f'Please insert {price}')
    print("You can pay only in \"Pennies - 0.01\", Nickles - 0.05, Dimes - 0.1 Quarter - 0.25. Type a name of coin you have put into machine... Please be aware that automat is keeping the change :)")
    machine["Geld"] += price
    while price > 0:
        coin = input(f"Price left: {price}Insert the coin :")
        price -= coins[coin]
    print("Proceeding...")
    return 1
def make_coffee():
    print("Makeing coffee, please stand by.")
    print("There you go! Thanks.")

while not to_do =="off":
    to_do = input("What would you like? (espresso/latte/cappuccino): ")
    if to_do == "espresso":
        if check_machine(espresso) == 1:
            if check_money(espresso) == 1:
                make_coffee()
    elif to_do == "latte":
        if check_machine(latte) == 1:
            if check_money(latte) == 1:
                make_coffee()
    elif to_do == "cappuccino":
        if check_machine(cappuccino) == 1:
            if check_money(cappuccino) == 1:
                make_coffee()
    elif to_do == "report":
        report()
    elif to_do == "off":
        print("Bye bye")

