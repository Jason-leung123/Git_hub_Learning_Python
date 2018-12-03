#---------------Simple Dictionary
alien_0 = {'color': 'green', 'points': 5} #This line will store information for color and points. Therefore when a print statement is made for color, it will print out 'green'
print(alien_0['color'])
print(alien_0['points'])

#---------------Working with Dictionaries
alien_0 = {'color': ['green ', 'big head'] } # This line stores one piece of information about ailen_0 namely the alien's color. The string 'color' is key in this dictionary
for alien in alien_0['color']:
    print(alien)

#---------------Accessing Values in a Dictionary
alien_0 = {'color' : 'green' , 'points' : 5}

new_points= alien_0['points']
print(f"You just earned {new_points} points!")

#Removing Key-values
alien_0 = {'color': 'green', 'points' : 5}
print(alien_0)
del alien_0['points'] #Using the del function in this example will delete the points out of the dictionary
print(alien_0)

#A Dictionary of similiar objects
favourite_languages = {
  'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }
print(favourite_languages['edward'])
print("Edward's favourite programming language is "
      + favourite_languages['edward'].title() +
      ".") # This line will add edward onto the the print statement because within this line, i am specifying edward to be seleceted from the list.
for name,language in favourite_languages.items(): #This line is similiar to line 43, with this command,
    print("Name: " + name)
    print("Programming Language: " + language)
# #----------------Looping through a dictionary
User_0 = {
    'username': 'Just-Jason123',
    'first name': 'jason',
    'last name' : 'leung',
}
for key, value in User_0.items(): #This line will create a loop for the dictionary. I've created names for the two variables that will hold the key and value. The dictionary followed by items() means that it will return a list of key-value pairs. The for loop then stores each of these values onto the pair
    print("\nKey: " + key)
    print("value: " + value)

#---------------Looping example
favourite_languages = {
    'jen': 'python',
    'jason': 'python',
    'Ricardo': 'html & CSS',
    'Dani': 'C',
    }
friends = ['jason', 'Dani']
for name in favourite_languages.keys():
    print(name.title())

    if name in friends:
        print("Hi \n " + name.title() + ", I know your favourite programming language is " + favourite_languages[name].title() + "!")

#-------------Another looping example
favourite_languages = {
    'jen': 'python',
    'jason': 'python',
    'Ricardo': 'html & CSS',
    'Dani': 'C',
    }
if 'solomon' not in favourite_languages.keys():
    programming_language = input("Solomon, what programming language do you like?\n")
    favourite_languages ['Solomon'] = programming_language

print(favourite_languages.values())
print(favourite_languages.keys())
print("The languages that have been mentioned:")
for language in set(favourite_languages.values()):
    print(language.title())

#--------------------Nesting
#A list of Dictionaries
aliens_0 = {'color' : 'green', 'points' : 5}
aliens_1 = {'color' : 'blue' , 'points' : 10}
aliens_2 = {'color' : 'yellow', 'points': 15}

aliens =[aliens_0, aliens_1, aliens_2]

for alien in aliens:
    print(alien)
#EXAMPLE
aliens = []
for alien_number in range(20):
    new_alien = {'color': 'green', 'points': 5, 'speed':'slow'}
    aliens.append(new_alien)
for alien_number1 in range(10):
    new1_alien = {'color': 'yellow', 'points': 10, 'speed': 'medium'}
    aliens.append(new1_alien)
for alien in aliens[0:3]: #This will select the first 3 items in the list aliens
    if alien['color'] =='green':
        alien['color'] ='yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    if alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:10]:
    print(alien)
print("...")
print("Total number of aliens: " + str(len(aliens)))

#List in a dictionary
pizza = {
    'crust' : 'thick',
    'toppings' : ['musgrooms', 'extra cheese'],
}
print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")

for topping in pizza['toppings']: #To print a list in a dictionary, you would use a for loop as it will check each value in the key
    print("\t" + topping)

#Another example
jason_favourite_workout = {
    'Upper body' : ['Bench press', 'Spider curls', 'Bent over row'],
    'Lower body' : ['Squats', 'Leg press', 'Lunges'],
    'Hypertrophy': ['Biceps', 'Triceps', 'Shoulders']
    }
for key, exercise in jason_favourite_workout.items():
    print("\tJason's does " + key + "and will do:")
    for exercises in exercise:
        print("\t" + exercises)

#Dictionary in a Dictionary
users = {
    'Jason Leung' : {
        'first name' : 'Jason',
        'last name' : 'Leung',
        'username' : 'Just-Jason123',
    },
    'Ricardo Lopez': {
        'first name' : 'Ricardo',
        'last name' : 'Lopez',
        'username' : 'RLopez12'
    }
}
for username, user_info in users.items():
    print("\nUser:" + username)
    full_name = user_info['first name'] + " " + user_info['last name']
    username_1 = user_info['username']

    print("\tFull name: " + full_name.title())
    print("\tUsername: " + username_1)

