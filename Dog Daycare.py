""" Program to do various functions for a dog care service
"""
import time


def drop_off():
    dog_name = input("Please enter dogs name here: ").lower()
    if dog_name:
        names_list.append(dog_name)


def pick_up():
    dog_name = input("Please enter your dogs name here: ").lower()
    if dog_name in names_list:
        print(f"{dog_name} has been removed from the roll")
        names_list.remove(dog_name)
    else:
        print("There is no dog on the roster with the name you have given me\n")


def calc_cost():
    dog_count = len(names_list)
    hours_to_look_after = int(input("How many hours are you looking after the dogs: "))
    global cost
    cost = dog_count / 12 * 22.5 * hours_to_look_after
    print("$", cost)


def print_roll():
    print(names_list)


# Main
names_list = []
option = 0
while option != 5:
    print("Welcome to DogsRus\n")
    print("Please choose an option below >>>>")
    print("1: Drop off a dog\n 2: Pick up a dog\n 3: Calculate cost\n 4: Print roll\n 5: Exit system")
    print()
    option = int(input("Please enter a number (1-5): "))
    print()

    if option == 1:
        drop_off()

    elif option == 2:
        pick_up()

    elif option == 3:
        calc_cost()

    elif option == 4:
        print(names_list)

    else:
        print("\nGoodbye...")
        time.sleep(3)
        quit()
