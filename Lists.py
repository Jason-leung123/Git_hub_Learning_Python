# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles) #This will print the entire list within one line
# print(bicycles[0].title()) #This will print the first word in the list as [0] symbolises the first word in the list
# print(bicycles[1])
# print(bicycles[-4]) #This will print the word that is the 4th word at the end of the list

#USING INDIVIDUAL VALUES FROM A LIST
# bicycle = ['trek', 'cannondale', 'redline', 'specialized']
# message = "My first bicycle was a " + bicycle[2].title() + "." #This line will pick the 3rd word from the list
# print(message)
#Example
# Name = ['Jason', 'Ricardo', 'Alvin']
# message = "Hello. My name is " + Name[0].upper() + "."
# print(message)

# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# motorcycles[0] = 'ducati' #This code replaces the first word of the list
# print(motorcycles)

# motorcycles.append('ducati') #This code add an item to the list at the end
# print(motorcycles)
# #Example
# Motorcycles=[]
# Motorcycles.append('Honda')
# Motorcycles.append('Yamaha') #From line 26 to 28 adds the three items to the list
# Motorcycles.append('ducati')
# print(Motorcycles)

#-------------Inserting items into a list--------------#
# motorcycles = ['honda', 'yamaha', 'suzuki']
# motorcycles.insert(0, 'ducati') #This code will insert an item at the first posistion, using [1] will set the item into 2nd posistion

#-------------Removing items off the list--------------#
# motorcycles = ['honda', 'yamaha', 'suzuki']
# del motorcycles[0] #This commands deletes an item off the list. You can target an item by using [0] or any digit
# print(motorcycles)
#-------------Reomving an item using pop()-------------#
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# popped_motorcycle = motorcycles.pop() #the pop function removes the last item of the list but it can also be worked on
# print(motorcycles)
# print(popped_motorcycle)
#------EXAMPLE-------#
#motorcycles = ['honda', 'yamaha', 'suzuki']
#last_owned = motorcycles.pop()
#print("The last motorcycle that i owned was " + last_owned.title() + ".")
#second_owned = motorcycles.pop(1) #This command line will remove and take the item from motorcycle and store it in the variable "second_owned"
#print("The second motorcycle that i owned was" + second_owned.title() + ".")
#------------Removing an item by Value-----------------#
# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)
# motorcycles.remove('ducati') #This line will remove 'ducati' from the list in line 52
# print(motorcycles)
#------EXAMPLE-------#
# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# too_expensive = 'ducati'
# motorcycles.remove(too_expensive)
# print(motorcycles)
# print("\nA " + too_expensive.title() + " is too expensive for me.") 
#What the example does is that it removes the ducati from the list but it is stored within a variable named too_expensive 
#------------Organizing a list------------------------#
#Animals =['Cat', 'Dog', 'Bird', 'Alligator']
# Animals.sort() #This commands sorts the list in alphabetical order
# print(Animals)
# Animals.sort(reverse=True) #This command will sort the list in reverse alphabetical order
# print(Animals)
#----------------------
# print("Here is the original list:")
# print(Animals)
# print("\nHere is the sorted list:")
# print(sorted(Animals))
# print("\nHere is the original list again:")
# print(Animals)
#From line 70 to 75 explains the way sorting a list works. When sorting a list, it will temporarily stick to the sorted list.
#-----------Printing List in Reverse Order------------#
# Animals =['Cat', 'Dog', 'Bird', 'Alligator']
# print(Animals)
# Animals.reverse() #This code will display the list in reverse alphabetical order
# print(Animals)
#----------Finding the length of a list---------------#
# Animals =['Cat', 'Dog', 'Bird', 'Alligator']
# print(len(Animals)) # This line displays how many items there are in the list.

