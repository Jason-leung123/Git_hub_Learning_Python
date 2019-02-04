class number():
    def __init__(self, num, num1):
        self.num = num
        self.num1 = num1
    def add_2_num(self):
        out = self.num + self.num1
        return out
    def subtract_2_num(self):
        out = self.num - self.num1
        return out
    def multiply_2_num(self):
        out = self.num * self.num1
        return out
    def divide_2_num(self):
        out = self.num / self.num1
        return out

import math        
try:
    question = int(input("How many numbers do you want to use?\n:"))

    if question == 1:
        print("Do you want to:\nFactorise\nSquare root\nSquare it")
        choice = input("Please type in one of the items in the list\n:")
        if choice == 'Factorise':
            num = int(input("Type in a number:"))
            fact = [math.factorial(num) for num in range(num)]
            print(fact)
        elif choice == 'Sqaure root':
            num = int(input("Type in a number:"))
            print(math.sqrt(num))           

    if question == 2:
        output = number(int(input("Type in a number:")),int(input("Type in another number:")))
        while True:
            s = input("If you want to add, press '+'\nIf you want to subract, press '-'\nIf you want to multiply, press '*'\nIf you want to divide, press '/'\n:")
            if s == '+':
                print(output.add_2_num())
                break
            elif s == '-':
                print(output.subtract_2_num())
                break
            elif s == '*':
                print(output.multiply_2_num())
                break
            elif s == '/':
                print(output.divide_2_num())
                break
            else:
                print("-----------------------------------------------\nThis value cannot be accepted. Please try agian\n-----------------------------------------------")
                continue

except:
    print("This value cannot be accepted")
