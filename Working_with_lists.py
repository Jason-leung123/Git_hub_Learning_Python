#--------Looping with lists----------#
magicians = ['alice', 'david', 'carolina']
for magician in magicians: #This command will define the loop. It tells python to pull the name from the list and store it in the vairable
    print(magician.title() + ", that was an amazing trick!") #This is combined with line 2 in which means for every word in the list, it will print that one item and will follow the code and print the next name
    print("For our next performer, please welcome..." + magician.title())
    print("Please show me your next trick, " + magician.title() + ".\n") #\n creates a blank line, making it look more neater
print("We hoped you enjoyed the show!") #When the loop finishes, it moves carries on the next set of commands

#--------Making Numerical Lists-----#
for value in range (1,5): #Remember to add the colon when making a for statement. This command will print 4 numbers when ranging from 1-5
    print(value)

numbers = list(range(1,6))
print(numbers)
even_numbers = list(range(2,11,1)) #The first value is the starting value while the last value is the increment meaning it will add to the starting value until it reaches to the second value
print(even_numbers)

squares = []
for value in range(1,11): #This is defining the value 
    square = value**2 #This line is the start of the loop meaning the value variable which is 1 will be times the power of 2. This process will continue until the value reaches 11
    squares.append(square) #Since the new value is in the square vairable, this command will add the new value onto the squares list.  
print(squares)

squares = [value**2 for value in range(1,11)] #This code is a simpler version from the previous however the way that this code works is that the expression is value**2, then the for loop is written in which the user can choose the range on how many numbers are added for calculation.
print(squares)


#-------Simple statistics----------#
digits = [1, 2, 3 ,4 ,5 ,6 ,7 ,8 ,9, 0]
min(digits) #This command will display the smallest number in the range
max(digits) #This command will display the higest number in the range
sum(digits) #This command will total all the numbers in the list

#-------Slicing a list-------------#
students =['Jason', 'Pops', 'Ben', 'Alvin', 'Ricardo']
print(students[0:3]) #This line will select the range from the first item to the 3rd item. Likewise, if the range was 1:3, it will select the second and third item.
print(students[:2]) #This line selects the first two items from the list
print(students[2:]) #This line will select everything from the list apart from the first 2 items 

#-------Looping Through a slice----#
Names = ['Jason', 'Ricardo', 'Homer', 'Charles', 'Eli']
print("Here are the first three people")
for name in Names[:3]: #This line will select the first three items from the list
    print(name.title())

# #-------Copying a list ------------#
my_foods = ['Pizza', 'Pasta', 'Chicken']
friend_foods = my_foods[:] #This line will select all the items on the list and with the variable, it will copy the items from the list into the new variable
my_foods.append('Poo') # This line will add an item to the list without it being copied because this line happens after the events of the lsit being copeid
friend_foods.append('cake')
print("My favourite foods are:")
print(my_foods)
print("\nMy friend's favourite foods are:")
print(friend_foods)

#--------Defining a Tuple------------#
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
for dimension in dimensions: #This loop means for one item in the list, it will print the item until it ends
    print(dimension)

#-------writing over a Tuple---------#
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
# What this entire code does is that the variable can change once it has already been set
