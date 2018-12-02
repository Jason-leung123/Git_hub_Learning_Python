# alien_0 = {'color': 'green', 'points':5}
# print(alien_0)

# alien_0['x_position'] = 0 # WIth this line, it adds a new key value onto the dictionary.
# alien_0['y_position'] = 25# This will add the item into the list.
# print(alien_0)

#Starting with an empty dictionary

# alien_0 = {}
# alien_0['color'] ='green' # By using this line, it will add the item within the paranthesis to the list
# alien_0['points'] = 5

# print(alien_0)

#Modifying Values in a Dictionary
# alien_0 = {'color': 'green'}
# print(f"The alien is now {alien_0['color']}.") # This line of code uses the dictionary 'color' to print the color of the alien

# alien_0['color'] ='blue' #This line will edit the old dictionary to the new one
# print(f"The alien is {alien_0['color']}.")

#EXAMPLE
# alien_0 ={'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print(f"Original x-position: {str(alien_0['x_position'])}.")
#
# #Now moving the alien to the right
# if alien_0['speed'] =='slow':
#     x_increment = 1
# elif alien_0['speed'] =='medium':
#     x_increment = 2
# else :
#     x_increment = 3
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print(f"New x-position {str(alien_0['x_position'])}")


#--------------Looping through all the keys in a dictionary
favourite_languages = {
    'jason' : 'python',
    'ricardo': 'ruby',
    'solomon': 'python',
    'dani' : 'C',
#     }
# friends = ['jason', 'dani'] #This line makes a list of 'friends' that i want to print a message to.
# for name in favourite_languages.keys(): # This line tell python to put all the keys from the dictionary on favourite_languages and store them on at a time in the variable called 'name'. Adding keys() isn't neccesasry when typing this code 
#     print(name.title())
#     if name in friends: # Here, I made a check to see whether the 'name' is in the list friends. If it is, then it prints a special greeting.
#         print(f"Hi {name.title()}, your favourite langauge is {favourite_languages[name].title()}!") #We use the name of the dictionary and the current value of 'name' as the key. This results in everyone names being printed but the names listed on 'friends' will have a message

