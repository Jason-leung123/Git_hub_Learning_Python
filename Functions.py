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

