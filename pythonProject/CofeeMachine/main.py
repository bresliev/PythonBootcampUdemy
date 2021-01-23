import data


def the_report():
    """This funciton prints the resources of the machine available at the moment"""
    print(f"Water: {data.resources['water']}ml")
    print(f"Milk: {data.resources['milk']}ml")
    print(f"Coffe: {data.resources['coffee']}")
    print(f"Money: {data.money}")


def money_input():
    money_input = 0.0
    money_input += float(input("How many quarters? : ")) * data.QUARTER
    money_input += float(input("How many dimes? : ")) * data.DIME
    money_input += float(input("How many nickles? : ")) * data.NICKLE
    money_input += float(input("How many pennies? : ")) * data.PENNY
    return money_input


def check_sufficient_resources(choice):

    for key, value in data.MENU[choice]["ingredients"].items():
        if data.MENU[choice]["ingredients"][key] > data.resources[key]:
            print(f"Sorry, there is not enough {key}")
            return False

    if data.MENU[choice]["cost"] > data.money:
        print(f"Please, provide some money for you have {data.money}, and you need {data.MENU[choice]['cost']}")
        data.money += money_input()
        check_sufficient_resources(choice)
        return True
    return True

def reduce_the_resources(choice):
    for key, value in data.MENU[choice]["ingredients"].items():
        data.resources[key] -= data.MENU[choice]["ingredients"][key]
    print(f"Sada jebeno imaš {data.money}")
    print(f"umanjeno za {data.MENU[choice]['cost']}")
    data.money = (data.money - data.MENU[choice]["cost"]).__round__(2)
    print(f"Sada jebeno imaš {data.money} umanjeno za data.MENU[choice]['cost']")


def make_a_coffee(choice):
    reduce_the_resources(choice)
    print(f"Here is your {choice}. Enjoiy it!")


def the_game():
    choice = "on"
    success = True

    while choice != "off" and success:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == "report":
            the_report()
        elif choice != "off":
            if check_sufficient_resources(choice):
                make_a_coffee(choice)


the_game()
