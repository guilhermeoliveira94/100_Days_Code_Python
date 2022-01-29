from database import MENU, COINS, resources


def select_product():
    print("Espresso $1,50")
    print("Latte $2,50")
    print("Cappuccino $3,00")
    product = input("What would you like?: ")
    product_value = MENU[product]['cost']
    return product_value


def insert_coins(valor_do_product):
    purchase = 0
    change = 0
    print("Please insert coins.")

    while purchase < valor_do_product:
        for c in COINS:
            temp = input(f"How many {c}?: ")
            purchase += int(temp) * COINS[c]
            print(f"You put a total of {purchase} in coins already.")
            if purchase >= valor_do_product:
                change += purchase - valor_do_product
                print(f"Your change is: {change}")
                return

    print(f"Your change is: {change}")


product_value = select_product()
insert_coins(product_value)


