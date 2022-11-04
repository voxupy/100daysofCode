from data import MENU, resources


def turnOff(answer):
    if answer == "off":
        print("machine is off.")


def format_data_resources(resources):
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']




def program():
    machine_is_running = True

    while machine_is_running:
        answer = input("What would you like?(espresso/latte/cappucino?")
        if answer == "off":
            turnOff(answer)
            machine_is_running = False


program()