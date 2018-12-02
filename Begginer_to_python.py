#-------------------Learning how to use Python part 1 (Jason Leung)-----------------------------#
# 
# 
#--------------------Variables and simple data types
name = "jason leung"
print(name.upper(),name.lower(),name.title())

#--------------------Using a variable with a string
first_name = "jason"
last_name = "leung"
full_name = first_name + " " + last_name
print("Hell0 " + full_name.title() +"!")

#-------------------Print Formatting
print("\tpython") #This code adds extra space

print("Languages:\nPython\nC\nJavaScript") #This line will create a new line when adding '\n' to a string

print("Languages:\n\tPython\n\tC\n\tJavaScript") #'n' and 't' can be combined to make a tab space as well create a list

favourite_language = 'Python ' #Python can detect whitespace, this means a space after a word
favourite_language.rstrip() #This command eliminates whitespace on the right side of the word
favourite_language.lstrip() #This command eliminates whitespace on the left side of the word
favourite_langauge.strip() #This command eliminates whitespace on both sides of the word

Message = "one of Python's strengths is its diverse community" #This is the correct way to use strings
Message = 'one of Python's strengths is its diverse community' #This is the incorrect way to use strings

#-------------------AVOIDING ERRORS WITH STR() FUNCTION

age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)
In line 31, it is classed as an integer therefore it won't print unless it is converted into a string. When adding 'str('variable)' it would convert an integer to a string
