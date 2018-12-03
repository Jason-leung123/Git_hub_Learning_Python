#--------------If statements------------#
cars = ['audi', 'bmw', 'subaru', 'honda'] #This line creates a list of cars

for car in cars: #This line will check each item in the variable 'cars'
    if car =='bmw': #This checks each item in the list in which means if the item in the list is to equal the string 'bmw', it will run the next line of code.
        print(car.upper())
    else: # This line means that if the other items on the list do not equal to the string 'bmw', it will run the code in line 8
        print(car.title())

#-------------Conditional Test

student = 'jason'
student == 'jason'
#In line 12, this creates a variable in which it holds a string named 'jason'. This is different to line 13 as using '==' makes a check to see if the variable which holds the string 'jason' is to equal the string 'jason'. This is true, whereas if one of the string were to be changed, it will change to false

#-------------Ignoring case when checking for equality
student = 'Jason'
student == 'jason' #This will turn into false as this do not equal to the string 'Jason' because it is case sensitive

student = 'Jason'
student.lower() == 'jason' #This will make the string in the variable student to a lowercase. This means that it will equal the string 'jason'

#--------------Checking for inequality
Food = 'Pizza'

if Food != 'Pasta': # This line is similiar to the equals sign('==') as the equal signs mean equal to, where as (!=) means DO NOT EQUAL TO.
    print("I like " + Food)
else:
    print("I like Pasta")

#--------------Numerical Comparisions
Age = 18
Age ==18 #Similiar to line 17, we set the variable as an integer in which the variable 'Age' will hold the value 18. This line means Age is equal to 18. This can be written as 18 equals to 18.


Answer = 17

if Answer != 42: #This line means that if the variable 'Answer' DOES NOT EQUAL to 42, it will run the next line of code
    print("That is not the correct answer")

#--------------Checking Multiple Conditions

>>>age_0 = 22
>>>age_1 = 18

>>>age_0 >= 21 and age_1 >= 21 #This line means that it checks to see if the age is greater than 21. With the age_0 variable being 22, it means it is greater than 22 and therefore this statement will be True however the other variable which is 18 is not greater than 21 and therefore the check will return to False.

# We can use Or statement to make a check for multiple conditions

>>>age_0 >= 21 or age _1 >= 21 #This line makes the overall condition of this statement to be True because one of the statement is True
>>>True
>>>age_0 = 18
>>>age_0 >= 21 or age _1 >= 21 #By now modifying the variable, this will change the overall condition as both statements are not greater than 22 which means that the overall conditions will become False.
>>>False

#-------------Checking whether a value is in a list
>>>requested_toppings = ['mushrooms', 'onions', 'pineapple']
>>>'mushrooms' in requested_toppings #When typing this line in Python, it will make a check to see if the string 'mushrooms' is in the list. The conditions is True
>>>True
>>>'pepperoni' in requested_toppings #This line checks to see if the string 'pepperoni' is in the list in which it is not therefore the overall conditions is False

#-------------Checking whether a value is Not in a list
Friends = ['Alvin', 'Ricardo', 'Kieran']
Not_friends = 'Peter'

if Not_friends not in Friends: # This line means that if the value 'Peter' is not in the list 'Friends', it will run the indented line because the conditions are True, Peter is not in the list.
    print(Not_friends.title() + ", do you want to become friends?")
    Friends.append(Not_friends)
print("My list of friends")
for Friend in Friends:
    print(Friend)

#-------------Boolean Expressions
game_active = True
game_over = False
#Booleans expression is another name of conditional tests. Booleans are another way to track the state of a program

#-------------Simple if-else Statements
age = 17
if age >=18: #This means that if the conditions are true meaning that if age is greater than 18, it will run the indented code in line 81 and 82
    print("You are old enough to vote!")
    print("Have you registered to vote yet")
else: #This line means that if the conditional test turns to False, the else block will run its code.
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you run 18")

#-------------Simple if-elif-else chain
#Instead of using the simple if-else  statement which only allows me to make 2 possible situations, using the if-elif-else chain can make multiple tests instaed of just 2.
age = 12

if age <4: #This line makes a test to see if the variable 'age' is under 4 years old. If the conditions were True, it will run the indented code and skip the rest of the tests. However, if the conditions were to be False, it will run the next test which is the 'Elif' statement
    print("Your entry fee is free")
elif age <18: #This line is similiar the if statement as when the beginning of the if statement fails, it will run the next test. In this example, the conditions are True meaning that it will run the indented code. If the conditions were False, it will run the next test, in this case, it will run the else statement.
    print("Your entry fee is £5")
else: #The else statement here marks the end of the if statement, meaning that if all the tests were to fail, Python will run the indented line.
    print("Your entry fee is £10")

#------------Not using the else Block
age = 12

if age <4:
    price = 0
elif age <18:
    price = 5
elif age < 65:
    price = 10
elif age >=65: #Using the else block isn't really neccessary because the else statement is the catchall statement meaning that it will match any conditions that wasn't specified in the if or elif test.
    price = 5

print("Your entry fee cost is £" + str(price) + ".") #The str() function changes the integer to a string therefore it will be able to print.

#-----------Testing Multiple Conditions
requested_toppings = ['mushrooms', 'extra cheese'] # Here, I started making a list

if 'mushrooms' in requested_toppings: #The if statement here checks to see 'mushrooms' is in the list, if it is, it will run the indented code in line 116
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings: #By using another if statement, it makes another check to see if the string 'pepperoni' appears in the list. This conditional test is false, therefore it will move onto the next line of code
    print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
#By using the if statement, it makes Python check the if statements whereas using elif or else blocks will run if the test fails. In the if statements, if it is True, it will not run the elif or else blocks, it will run the next line of code. Therefore by adding multiple if statements, it will test multiple conditions.
print("\nFinished making your pizza!")

#-----------Checking for special items
requested_toppings = ['mushrooms', 'extra cheese', 'pepperoni']

for requested_topping in requested_toppings:
    if requested_topping == 'pepperoni': #This line means if the list contains an item 'pepperoni', it will run the indented line.
        print("Sorry, we ran out of pepperonis right now.")
    else: #This line ensures means that if the conditions are False, it will make a print statement.
        print("Adding " + requested_topping + ".")

#----------Checking That a list is not empty
requested_toppings = []# This line creates an empty list

if requested_toppings: # Instead of using a for loop, I would do a check. When the name of the lise is used in an if statement, Python returns True if the list contains at least one item. This also means that if there is no items in the list, it will evalutate to False
    for requested_topping in requested_toppings: #This does another check meaning for every item in the list, it will print the indented code in line 138
        print("adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else: #This means that if the conditional test on the if statement is False, it will run the else statement. The reason why the if statement is False in this example is because there is no values in the list. If there were values in the list, it will turn to True
    print("Are you sure you want a plain pizza?")

#----------Using Multiple Lists

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese'] #In this line, i defined a list

requested_toppings = ['mushrooms', 'french fries'] #I also made a list that a customer had ordered

for requested_topping in requested_toppings: #This line makes a loop and check for each item in the list.
    if requested_topping in available_toppings: #This line checks to see if the requested_topping matches the available_toppings and if so, it will mean the conditional test is True. For example, one of the item in requested_toppings is 'mushrooms', this means that if 'mushrooms' is in available_toppings, the conditional test will be True and then it will rn the indented lines
        print("Adding " + requested_topping + ".")
    else: #If the requested_topping is not in the list of available toppings, it will run the else block.
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza")
