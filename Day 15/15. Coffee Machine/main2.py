from database import MENU, COINS, resources


def select_product():
    print("Espresso $1,50")
    print("Latte $2,50")
    print("Cappuccino $3,00")
    product = input("What would you like?: ")
    if product == "off":
        exit()
    elif product == "resources":
        print(resources)
        select_product()
    else:
        if check_resources(product):
            return product


def check_resources(product):
    print(MENU[product]["ingredients"])
    return True


def insert_coins(product):
    product_value = MENU[product]['cost']
    purchase = 0
    change = 0
    print("Please insert coins.")

    while purchase < product_value:
        for c in COINS:
            temp = input(f"How many {c}?: ")
            purchase += int(temp) * COINS[c]
            print(f"You put a total of {purchase} in coins already.")
            if purchase >= product_value:
                change += purchase - product_value
                print(f"Your change is: {change}")
                return

    print(f"Your change is: {change}")


product = select_product()
insert_coins(product)


