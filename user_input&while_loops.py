#---------------Simple input()
greetings = input("If you type something here, it will repeat the input again")
print(greetings)

#---------------Writing clear prompts
name = input("Please enter your name")
print(f"Hello, {name}!")

#--------------Using int() to accept numerical input
height = input("What is your height, in inches\n")
height = int(height) #This line means that when a user inputs a number, it will be a string. This means that I have to convert it from a string to an integer, to do this we use int()

if height >= 40:
    print("You are tall")
else:
    print("You are small")

#--------------Modulo Operator
#The modulo operator(%) is an operator which divides a number by another number and returns the remainder:
#Typing '4%3' into python on the terminal will result in providing the answer

#Example
number = int(input("Enter a number and this program will detect if its odd or even\n"))

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd")

#-------------While loops
current_number = 1 
while current_number <=5: #This means that if the current number is smaller than 5, it will continue to loop until the number is greater than 5
    print(current_number)
    current_number +=1

#-------------Letting the User choose to quit the while statement
prompt = "\nYou can write anything and this program will repeat it back to you:"
prompt +="\nEnter 'quit' to end the program.\n" #This line defines the message which gives two options for the user.

message = "" #By setting the user_input to have quotation marks means that it will be able to store information.
while message != 'quit': #This line means that if the user input is not equal to 'quit', then it will continue to loop until the user types 'quit'
    message = input(prompt)
    
    if message != 'quit': # This line means that if the user inputs 'quit', it will not print it
      print(message)

#-------------Using Flags
prompt = "\nYou can write anything and this program will repeat it back to you:"
prompt +="\nEnter 'quit' to end the program.\n"

active = True #I set the variable active to 'True', This will make the while statement simpler as there will be no comparrison with the while statement. As long as the active variable remains True, it will continue to loop
while active: #This means while True, which also means that it will continue to loop until  we set the active variable to False
    message = input(prompt)

    if message == 'quit': #This line means that if the message is to equal the string 'quit', it will change the active state to False, meaning that it will no longer loop
        active = False
    else: #This means that if the message does not equal to 'quit', it will print the user inputs
        print(message)

#-------------Using break to exit a loop
prompt = "\nType in your favourite food:"
prompt +="\nEnter 'quit' to end the program.\n"

while True: # This line will continue to run unless it reaches a break statement
    message = input(prompt)

    if message == 'quit':
        print("You have stopped the loop")
        break #This means that if the user were to input 'quit', it will break the loop. 
    else:
        print("I like to eat " + message + "!")

#-----------Using continue in a loop
current_number = 0
while current_number <10: #Here is using the while statement as a comparision. It means that if the current_number is smaller than 10, it will run the loop
    current_number += 1
    if current_number % 2 == 0:
        continue #This line means that if the current_number is divisible by 2 and is even, it will ignore the rest of the loop go back to the beginning of the loop and make a check again. This program means that it will only print odd numbers
    print(current_number)

#----------Making infinite loops
x = 1
while x: #Since there is no comparision or no if statements to stop the loop, it will continue to run forever
    x += 1
    print(x)

#----------Preventing infinite loops
x = 1
while x <= 5: #This line makes a comparision which means that if the variable x is smaller than 5, it will increment the current number by 1 and will continue to loop until x is greater than 5
    print(x)    
    x +=1
    
#---------Using a while loop with lists and dictionaries
unconfirmed_users = ['jason', 'ricardo', 'ben'] #In this line, i created a list
confirmed_users = [] #Another list is created but it is empty
while unconfirmed_users: #The while loop here means that it will continue to loop until there is no items in the variable unconfirmed_users
    current_user = unconfirmed_users.pop() # Within the while loop, the pop function removes and returns the last item in the list at a time meaning that an item will be removed from the list and stored in the current_user variable

    print("Verifying user: " + current_user.title()) 
    confirmed_users.append(current_user) #This line will add the variable current_user into the confirmed user lists. Since the variable is being modified, it keeps changing and will not add a new item into the variable   
print("\nUsers that are confirmed:")
for confirmed_user in confirmed_users: # This line checks for every item in confirmed_user, it will run a print statement
    print(confirmed_user.title())

#--------Removing All instances of specific values from a list
Game_platforms = ['Playstation 4', 'Xbox', 'PC', 'Xbox', 'Xbox', 'Ninentdo Switch']
print()

while 'Xbox' in Game_platforms: #This line means that as long as Xbox remains in the list, it will run a loop.  
    Game_platforms.remove('Xbox') #This line will remove 1 item at a time. This means that the loop will break when the item 'Xbox' is no longer in the list
print(Game_platforms)

#-------Filling a Dictionary with User input
responses = {}


polling_active = True 
while polling_active:# This line means that it will continue to loop unless it is changed to false

    name = input("\nWhat is your name? \n") # When a user input their answer, it will store it into the 'name' variable
    response = input("What do you like to eat? \n") #Similiar to line 120, a user will input their answer and it will be stored in the variable 'response'

    responses[name] = response # This line stores the information into the dictionary. Meaning that the name is the key and the response is the value

    repeat = input("Would you like to let another person respond? (Yes/No) ") # 
    if repeat == 'No' or 'no': #This line means that if the user were to input 'no', this will end the loop as it sets the active set to False and follow the next line of code 
        polling_active = False
print("\n--- Poll Results ---")
for name, response in responses.items(): #What this line does is that for every item in the dictionary, it will continue to make a print statement
    print(name + " would like to eat " + response + ".")



