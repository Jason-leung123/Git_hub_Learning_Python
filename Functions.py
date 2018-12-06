#--------------------Functions

#-----------Defining a Function
# def greet_user(): # In this line, it uses a keyword called 'def', it tells Python that i'm defining a function. The 'def' function means that it tells python the name of the function and what kind of information the function needs to do its job. The paranthesis holds that information
#     """Display a simple greeting.""" # This line is a comment called docstring which describes what the function does. Docstrings are enclosed in triple quotes.
#     print("Hello") # This is the only line of actual code in the body of this function. This means that 'greet_user()' has one job and that is to print("Hello")

# greet_user() # To call a function, you could write it as it is. 

#--------------------Passing information to a Function 
# def greet_user(username): #By entering the value 'username' into the parantheses, it will allow the function to accept any value of username i specify.
#     """Display a simple greeting"""
#     print("Hello, " + username.title() + "!")

# greet_user(input('What is your name?\n')) # This line calls on 'greet_user()' in which by entering a name into the paranthesis will call upon the function.

#--------------------Arguements and Parameters
#The variable 'username' in the definition of greet_user() is an example of a parameter. It is a piece of information the function eeds to its job. The value (input()) is an arguement. A piece of information that is passed from a function call to a function.
# In the example of 'Passing information to a Function', the 'input()' is the arguement that was passed to the function 'greet_user() and the value was stored in the parameter 'username'

#---------Passing Arguements
#If a function definition can have multiple parameters, this will also mean the function call will need multiple arguements. 

#----Posistional Arguements
#When you call a function, Python must match each arguement in the function call with a parameter in the function definition. One way to do this is by making a posistional arguement.
# def describe_pet(animal_type, pet_name): # This line means that I need to provide an animal type and name at that order. This means that the string 'hamster' in line 30 will be stored in the animal_type and 'harry' is stored in pet_name
#     print("\nI have a " + animal_type + ".")
#     print("\nMy " + animal_type + "'s name is " + pet_name.title() + ".")

# describe_pet('hamster', 'harry') # This line calls upon describe_pet, this is matched to the function definition parameter. 

#The order in positional arguements matters as there is a possibility to get the wrong results if you were to mix up the order of the arguements in a function call. 

#----Multiple Function calls
# def describe_pet(animal_type, pet_name): 
#     print("\nI have a " + animal_type + ".")
#     print("\nMy " + animal_type + "'s name is " + pet_name.title() + ".")

# describe_pet('hamster', 'harry') 
# describe_pet('cat', 'carly') # Same with the previous example, we matched the two arguements with the parameters. We can use multiple function calls by using the function call again.  

# #Another Example
# def make_shirt(size, text):
#     print("Size: " + size.title())
#     print("text: " + text)

# make_shirt('small', 'I like potatoes')
#----Keyword Arguements
# A keyword arguement is a name-value pair that you pass to a function. This means that you would directly associate the name and the value within the aruement. This is more effective than position arguements. 

# def describe_pet(animal_type, pet_name): 
#     print("\nI have a " + animal_type + ".")
#     print("\nMy " + animal_type + "'s name is " + pet_name.title() + ".")

# describe_pet(animal_type = 'fish', pet_name='george') 

#The function in line 51 stays the same, the only difference is in line 49. In the arguement, I tell python which arguement should be matched with therefore it knows the animal_type is matched with fish. 

#Another Example
# def make_shirt(size, text):
#     print("Size: " + size.title())
#     print("text: " + text.title())

# make_shirt(text = 'pizza', size = 'large')

#----Default Values
#When writing a function, you can define a default value for each parameter. When an arguement is provided to a parameter when the parameter has a default value, it will use the arguement value. 

# def describe_pet(pet_name, animal_type = 'dog'): 
#     print("\nI have a " + animal_type + ".")
#     print("\nMy " + animal_type + "'s name is " + pet_name.title() + ".")

# describe_pet(pet_name='george') 

#The change in this block of code is that we changed the animal_type to have a default value of 'dog'. The order of the parameters in the function def had to be changed because the default value makes it specify a type of animal as an arguement. The only arguement left in the function call is the pet's name. This means that python will think it as a positional arguement. To fix this, I placed the pets_name in front of animal_type

#Another Example
# def describe_city(name_of_city, country):
#     print(name_of_city + " is in " + country)
# describe_city("London", "UK")

#-Equivalent Function Calls
# def describe_pet(pet_name, animal_type = 'dog'):
#     print("\nI have a " + animal_type + ".")
#     print("\nMy " + animal_type + "'s name is " + pet_name.title() + ".")

# # A dog named Jason 
# describe_pet('Jason')
# describe_pet(pet_name ='willie')

# # A cat named Lizz
# describe_pet('lizz', 'cat')
# describe_pet(pet_name = 'lizz', animal_type = 'cat')
# describe_pet(animal_type = 'cat', pet_name = 'lizz')

#There are multiple ways to make a function call but also have the same output.

#--------------------Return Values
#A function can also process some data and then return a value or a set of values.
#The return statement takes a value from inside a function and sends it back to the line that called the function.

# def formatted_name(first_name, last_name): #Here i made 2 parameters and they are first name and last name.
#     full_name = first_name + " " + last_name #This line combines the two parameters together and stores it in a variable
#     return full_name.title() #
#
# musician = get_formatted_name('jimi', 'hendrix') #When calling a function that returns a value, you need to provide a variable where the return value can be stored.
# print(musician)

#Another Example
# def city_country(city, country):
#     full_city_country = city + " " + country
#     return full_city_country.title()
#
# place = city_country('london', 'UK')
# print(place)

#----Making an argument optional
# def formatted_name(first_name, last_name, middle_name=''): # first name and last name are listed first. The middle name is optional so its listed last and has a default value of a empty string.
#     if middle_name: # This line checks to see if a middle_name has been provided. Python interprets the non-empty string as True.
#         full_name = first_name + ' ' + middle_name + ' ' + last_name
#     else: #If a middle name is not provided, this will result the test to be false. This will run the else statement
#         full_name = first_name + ' ' + last_name
#     return full_name.title()
# musician = formatted_name('linda', 'fee')
# print(musician)
#
# musician = formatted_name('jason', 'leung', 'von')
# print(musician)

#Another Example
# def make_album(artist_name, album_title, number_of_tracks):
#     if number_of_tracks:
#         full_album = artist_name.title() + " - " + album_title + " - " + number_of_tracks
#     else:
#         full_album = artist_name.title() + " - " + album_title
#     return full_album
# album = make_album('john lennon', 'Top 50 charts', '50')
# print(album)

#----Returning a Dictionary
# def build_person(first_name, last_name, age=''):
#     person = {'first': first_name, 'last': last_name} # the function takes in the first and last name. It takes these values into a dictionary. first_name is stored with the key 'first', the value of last_name is stored with the key 'last'.
#     if age:
#         person['age'] = age
#     return person # The entire dictionary representing the person is returned in this line.
# musician = build_person('jason', 'leung', age=18)
# print(musician) # The return value is printed.

#----Using a function with a while loop
# def formatted_name(first_name, last_name):
#     full_name = first_name + " " + last_name
#     return full_name.title()
# while True: # This line makes the loop forever
#     print("\nPlease enter your name:")
#     print("(enter 'q' at any time to quit)")
#
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
#     formatted_names = formatted_name(f_name, l_name)
#     print("\nHello, " + formatted_names + "!")

#Another example
def make_album(artist_name, album_title):
    albums = {}
    albums["artist's name"]= artist_name
    albums["album_title"]= album_title
    return albums
while True:
    print("\nEnter an album's artist and title")
    print("\nTo quit, press 'q'")
    artist = input("Artist: ")
    if artist == 'q':
        break
    name_of_album = input('Album: ')
    if name_of_album == 'q':
        break
    name_and_album = make_album(artist, name_of_album)
    print(name_and_album)
    
#-------------------Passing a list
# def greet_user(names):
#     for name in names:
#         msg = "Hello, " + name.title() + "!"
#         print(msg)
# people = ['jason', 'alvin', 'george'] # In this line, i defined a list of names. Then i pass the 'people' to greet_user() in the function call
# greet_user(people) #This line is a function call in which in this example will create a greeting message for each item in the list. 

#Another Example
# def magicians(names):
#     for name in names:
#         greet = "Please welcome, " + name.title()
#         print(greet)
# magician = ['john', 'ian', 'tom']
# magicians(magician)

#----Modifying a list in a function
# def print_models(unprinted_desings, completed_models): #Here, i defined the function with two parametes. A list that need to printed and a list of completed models. This entire function makes it so that for every item in unprinted_designs, it will add it to the completed_models.
#     while unprinted_desings:
#         current_design = unprinted_desings.pop()
#         print("Printing model: " + current_design)
#         completed_models.append(current_design)

# def show_completed_models(completed_models): #This function has one parameter. show_completed_models() would display the name of each model that was printed
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

#Another Example
# def show_magicians(names):
#     for name in names:
#         greet = "Please welcome, " + name.title()
#         print(greet)
# magician = ['john', 'ian', 'tom']
# show_magicians(magician)
# def make_great(great):
#     for greats in great:
#         Great = "The Great " + greats.title()
#         print(Great)
# make_great(magician)
