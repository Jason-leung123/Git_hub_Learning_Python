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
class number2():
    def __init__(self,num2,num3,num4):
        self.num2 = num2
        self.num3 = num3
        self.num4 = num4
    def add_and_add(self):
        out = self.num2 + self.num3 + self.num4
        return out
    def add_and_subtract(self):
        out = self.num2 + self.num3 - self.num4
        return out
    def add_and_times(self):
        out = self.num2 + self.num3 * self.num4
        return out
    def add_and_divide(self):
        out = self.num3 + self.num3 / self.num4
        return out
    def subtract_and_add(self):
        out = self.num2 - self.num3 + self.num4
        return out
    def subtract_and_subtract(self):
        out = self.num2 - self.num3 - self.num4
        return out
    def subtract_and_times(self):
        out = self.num2 - self.num3 * self.num4
        return out 
    def subtract_and_divide(self):
        out = self.num2 - self.num3 * self.num4
        return out
    def times_and_add(self):
        out = self.num2 * self.num3 + self.num4
        return out 
    def times_and_subract(self):
        out = self.num2 * self.num3 - self.num4
        return out
    def times_and_times(self):
        out = self.num2 * self.num3 * self.num4
        return out
    def times_and_divide(self):
        out = self.num2 * self.num3 / self.num4 
        return out
    def divide_and_add(self):
        out = self.num2 / self.num3 + self.num4
        return out
    def divide_and_subract(self):
        out = self.num2 / self.num3 - self.num4
        return out
    def divide_and_times(self):
        out = self.num2 / self.num3 * self.num4
        return out 
    def divide_and_divide(self):
        out = self.num2 / self.num3 * self.num4
        return out
import math        
try:
    question = int(input("How many numbers do you want to use?\n:"))

    if question == 1:
        print("To Factorise, type in = %\nTo Square root, type in: $\nTo Square it, type in: !")
        choice = input("Please type in one of the items in the list\n:")
        if choice == '%':
            num = int(input("Type in a number:")) 
            fact = [math.factorial(num) for num in range(num)]
            print(fact)
        elif choice == '$': 
            num = int(input("Type in a number:"))
            print(math.sqrt(num))
        elif choice == '!':
            num = int(input("Type in a number:"))
            print(num ** num)

    if question == 2:
        output = number(int(input("Type in a number:")),int(input("Type in another number:")))
        while True:
            s = input("If you want to add, press '1'\nIf you want to subract, press '2'\nIf you want to multiply, press '3'\nIf you want to divide, press '4'\n:")
            if s == '1':
                print(output.add_2_num())
                break
            elif s == '2':
                print(output.subtract_2_num())
                break
            elif s == '3':
                print(output.multiply_2_num())
                break
            elif s == '4':
                print(output.divide_2_num())
                break
            else:
                print("-----------------------------------------------\nThis value cannot be accepted. Please try agian\n-----------------------------------------------")
                continue
    if question == 3:
        output = number2(int(input("Type in a number:")),int(input("Type in another number:")),int(input("Type in the last number:")))
        print("What would you like to do with the first two numbers:\n1.Add\n2.Subtract\n3.Times\n4.Divide\nPick a number you want to use.")
        answer = int(input(":"))
        if answer == 1:
            print("What would yo like to do with the last two numbers:\n1.Add\n2.Subtract\n3.Times\n4.Divide")
            answer1 = int(input((":"))
            if answer1 ==1:
                

except:
    print("This value cannot be accepted")