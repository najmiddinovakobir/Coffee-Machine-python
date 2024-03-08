from data import MENU
import art
import color

cost = 0
water = 0
milk = 0
coffee = 0


def get_form(number):
    global milk
    global coffee
    global water
    global cost
    cost = MENU[number]['cost']
    water = MENU[number]['ingredients']['water']
    coffee = MENU[number]['ingredients']['coffee']
    if number == 2 or number == 3:
        milk = MENU[number]['ingredients']['milk']
        print(f'''Ingredients:
Cost: {cost}
Coffee: {coffee}
Water: {water}
Milk: {milk}''')
    else:
        print(f'''Ingredients:
Cost: {cost}
Coffee: {coffee}
Water: {water}''')


def sale_coffee():
    max_water = 300
    max_milk = 200
    max_coffee = 100
    flag = True
    print(art.coffee_logo)
    while flag:
        print("Choose your coffee:")
        print(f"{color.YELLOW}1. Espresso - $1.5{color.END}")
        print(f"{color.BROWN}2. Latte - $2.5{color.END}")
        print(f"{color.BROWN}3. Cappuccino - $3.0{color.END}")
        print(f'{color.RED}4. OFF the machine{color.END}')
        number = int(input(f"{color.END}Enter your choice: {color.END}"))
        if number == 1 or number == 2 or number == 3 and number == 4:
            dollar = float(input(f'{color.END}Enter your Amount With dollar: ${color.END}'))
            get_form(number)
            if number == 1:
                if max_water >= water and max_coffee >= coffee and dollar >= cost:
                    print(f"{color.YELLOW}This is your Espresso{color.END}")
                    max_water -= water
                    max_coffee -= coffee
                    if dollar >= cost:
                        print(f"{color.LIGHT_BLUE}Ok! Thank You for Buy{color.END}")
                        money_back = round(dollar - cost, 1)
                        print(f"{color.LIGHT_BLUE}Ok! Thank You for Buy{color.END}")
                        print(f'{color.LIGHT_PURPLE}Your money back is {money_back}{color.END}')
                else:
                    if dollar < cost:
                        print(f"{color.LIGHT_GRAY}Your money is not enough you you pay {cost}{color.END}")
                    else:
                        if max_water < water:
                            print(f'Water is not enough')
                        elif max_coffee < coffee:
                            print(f'Coffee is not enough')
                        print('Machine Is off because Ingredients not enough')
                        break
            elif number == 2:
                if max_water >= water and max_coffee >= coffee and dollar >= cost and max_milk >= milk:
                    print(f"{color.BROWN}This is your Latte{color.END}")
                    max_water -= water
                    max_coffee -= coffee
                    max_milk -= milk
                    if dollar == cost:
                        print(f"{color.LIGHT_BLUE}Ok! Thank You for Buy{color.END}")
                    else:
                        money_back = round(dollar - cost, 1)
                        print(f"{color.LIGHT_BLUE}Ok! Thank You for Buy{color.END}")
                        print(f'{color.LIGHT_PURPLE}Your money back is {money_back}{color.END}')
                else:
                    if dollar < cost:
                        print(f"{color.LIGHT_GRAY}Your money is not enough you you pay {cost}{color.END}")
                    else:
                        if max_water < water:
                            print(f'Water is not enough')
                        elif max_coffee < coffee:
                            print(f'Coffee is not enough')
                        elif max_milk < milk:
                            print(f'Milk is not enough')
            elif number == 3:
                if max_water >= water and max_coffee >= coffee and dollar >= cost and max_milk >= milk:
                    print("This is your Cappuccino")
                    max_water -= water
                    max_coffee -= coffee
                    max_milk -= milk
                    if dollar == cost:
                        print(f'{color.LIGHT_BLUE}Ok! Thank You for Buy{color.END}')
                    else:
                        money_back = round(dollar - cost, 1)
                        print(f"{color.LIGHT_BLUE}Ok! Thank You for Buy{color.END}")
                        print(f'{color.LIGHT_PURPLE}Your money back is {money_back}{color.END}')
                else:
                    if dollar < cost:
                        print(f"{color.LIGHT_PURPLE}Your money back is {dollar - cost}{color.END}")
                    else:
                        if max_water < water:
                            print(f'Water is not enough')
                        elif max_coffee < coffee:
                            print(f'Coffee is not enough')
                        elif max_milk < milk:
                            print(f'Milk is not enough')
            elif number == 4:
                print("Off")
                break
        else:
            print("Please Enter the Valid num")


sale_coffee()
