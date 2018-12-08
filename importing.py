def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) +
        "-inch pizza with the following toppings:")
    for topping in toppings:
        print("-" + topping)

def workout(name, age, **details):
    gym = {}
    gym['Name: '] = name
    gym['Age'] = age
    for key, value in details.items():
        gym[key] = value
    print(gym)
    return gym
