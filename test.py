from data import MENU


def get_form(num):
    cost = MENU[number]['cost']
    water = MENU[number]['ingredients']['water']
    coffee = MENU[number]['ingredients']['coffee']
    if num == 2 or num == 3:
        milk = MENU[number]['ingredients']['milk']
        return f'milk {milk} coffee {coffee} water {water} name {cost}'
    else:
        return f'coffee {coffee} water {water} name {cost}'


number = int(input("1 or 2 or 3 "))
print(get_form(number))

