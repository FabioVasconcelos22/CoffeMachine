import utils

isOn = True

water = utils.resources["water"]
milk = utils.resources["milk"]
coffee = utils.resources["coffee"]
money = 10

def GetResourceValue (product, resource):
    if resource in utils.MENU[product]["ingredients"]:
        return utils.MENU[product]["ingredients"][resource]
    else:
        return 0
def GetResourceAvailability (product, resource):
    if resource in utils.MENU[product]["ingredients"]:
        return utils.MENU[product]["ingredients"][resource] <= utils.resources[resource]
    return True

def GetWaterAvailability(product):
    return GetResourceAvailability(product, "water")
def GetCoffeeAvailability(product):
    return GetResourceAvailability(product, "coffee")
def GetMilkAvailability(product):
    return GetResourceAvailability(product, "milk")

def GetAvailability(product):
    if product == "espresso" or product == "latte" or product == "cappuccino":
        if not GetWaterAvailability(product):
            print("Sorry there is not enough water.")
            return False
        if not GetCoffeeAvailability(product):
            print("Sorry there is not enough coffee.")
            return False
        if not GetMilkAvailability(product):
            print("Sorry there is not enough milk.")
            return False
    else:
        print("Product is not valid")
        return False

    return True


def ReadCoins():
    quarters = int(input("Insert quarters: "))
    dimes = int(input("Insert dimes: "))
    nickles = int(input("Insert nickles: "))
    pennies = int(input("Insert pennies: "))

    return quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01


def isEnoughMoney(valueInserted, product):
    result = valueInserted >= utils.MENU[product]["cost"]
    if not result:
        print("Sorry that's not enough money. Money refunded.")
        return False
    return True


while isOn:
    request = input("What would you like? (espresso/latte/cappuccino):")

    if request == "off":
        isOn = False
        break

    if request == "report":
        print(f"Water: {water} ml"
              f"Milk: {milk}ml"
              f"Coffee: {coffee}g"
              f"Money: ${money}")

    else:
        available = GetAvailability(request)

        if available:
            valueInserted = ReadCoins()
            transactionStatus = isEnoughMoney(valueInserted, request)
            if transactionStatus:
                exchange = valueInserted - utils.MENU[request]["cost"]
                money += utils.MENU[request]["cost"]
                water -= GetResourceValue(request, "water")
                milk -= GetResourceValue(request, "milk")
                coffee -= GetResourceValue(request, "coffee")

                if exchange > 0:
                    print(f"Here is ${exchange} dollars in change.")

                print(f"Here is your {request}. Enjoy!")
