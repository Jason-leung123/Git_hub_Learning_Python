#----------------------Classes---------------------# 

#--------------Creating and Using a class

# class Dog(): #In this line, I defined a class called Dog. 
#     """A simple attempt to model a dog."""

#     def __init__(self, name, age): #A function that is part of a class is a method. the ___init___() method is a special method that Python runs automatically whenever you create a new instance based on the Dog class. I define the __init__() method to have three parameters. The self parameter is required in the method definition and it must come first before the other parameters. When Python calls this __init__() method later (to create an instance of Dog) the method call will automatically pass 'self', which is a reference to the instance iteself. Every method call associated with a class automatically passes self, which is a reference to the instance iteself. It gives the individual instance access to the attributes and methods in the class. When I make an instance of 'Dog', Python will call the __init__() method from the Dog Class. We'll pass Dog() a name and age as arguements; self is passed automatically, so we don't need to pass it. Whenever we want to make an instance from the Dog class, we'll provide values for only the last two parameters, name and age. 
#         """Name and age attribures."""
#         self.name = name #The two variables each have the prefix 'self'. Any variable prefixed with self is available to every method in the class, and it can also be able to access these variables through any instance created from the class. self.name = name takes the value stored in the parameter name and stores it in the variable 'name'. This is then attatched to the instance being created. 
#         self.age = age

#     def sit(self): #The Dog class has two other methods defiend:sit() and roll_over(). Because these methods don't need additional information like a name or age, I define them to have one parameter, 'self'. The instances I create later will have access to thees methods. 
#         print(self.name.title() + " is now sitting")

#     def roll_over(self):
#         print(self.name.title() + " rolled over!")

# my_dog = Dog('jason', 2) #This line tells Python to create a dog whose name is 'Jason' and age is 2. When Python reads this line, it calls the __init__() method in 'Dog' with the arguements 'jason' and 2. The __init__() method creates an instance representing this particular dog and sets the name and age attributes using the values I provided. The __init__() method has no return statement but Python automatically returns the instance representing this dog. I store the instance in the variable my_dog. 

# print("My dog's name is " + my_dog.name.title() + ".") # To access the attributes of an instance, you would write the variable, then use a dot notation, and then the attribute.
# print("My dog's age is " + str(my_dog.age) + " years old.") # This line is same as line 21. Line 21 creates a print statement which makes the name 'Jason' and the second print statment converts 2 to a string. 

# #To call a method, you would give the name of the instance. So in this example i would use my_dog and then the method I want to call. When python reads line 25, it looks for the method sit() in the class Dog and runs that code. 

# my_dog.sit()
# my_dog.roll_over()

# #You can also create as many instances from a class you need

# your_dog = Dog('Steph', 10)
# friend_dog = Dog('carly', 5)

# print("Your dog name is " + your_dog.name.title() + ".")
# print("Your dog's age is " + str(your_dog.age) + " years old.")

# print("My friend's dog name is " + friend_dog.name + ".")
# print("My friend's dog age is " + str(friend_dog.age) + ".")

#Example A
# class Restaurant():
#     def __init__(self, name, type):
#         self.name = name
#         self.type = type
    
#     def describe_restaurant(self):
#         print("The name of the restaurant is called " + self.name + ".")
#         print("The type of restuaruant is a " + self.type + ".")
    
#     def open_restaurant(self):
#         print(self.name + " is open")

# rest1 = Restaurant('McDonalds', 'Fast Food')
# print(rest1.name, "\n"+ rest1.type)
# rest1.open_restaurant()
# rest1.describe_restaurant()

# rest2 = Restaurant('Bella Italia', 'Italian')
# print(rest2.name, "\n" + rest2.type)
# rest2.open_restaurant()
# rest2.describe_restaurant()

#Example B
# class Users():
#     def __init__(self, first_name, last_name, age):
#         self.first = first_name
#         self.last = last_name
#         self.age = age
#     def describe_user(self):
#         print(" You are " + str(self.age) + " years old")
#     def greet_user(self):
#         print("Hello " + self.first.title() + " " + self.last.title())


# user1 = Users('jason', 'leung', 18)
# user1.greet_user()
# user1.describe_user()

#----------------------Working with classes and instances

