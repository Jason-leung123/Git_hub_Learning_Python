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
        print("To Factorise, type in = 1\nTo Square root, type in: 2\nTo Square it, type in: 3")
        choice = input("Please type in one of the items in the list\n:")
        if choice == '1':
            num = int(input("Type in a number:")) 
            fact = [math.factorial(num) for num in range(num)]
            print(fact)
        elif choice == '2': 
            num = int(input("Type in a number:"))
            print(math.sqrt(num))
        elif choice == '3':
            num = int(input("Type in a number:"))
            print(num ** num)

    if question == 2:
        output = number(int(input("Type in a number:")),int(input("Type in another number:")))
        while True:
            s = input("If you want to add, press '1'\nIf you want to subract, press '2'\nIf you want to multiply, press '3'\nIf you want to divide, press '4'\n:")
            if s == '1':
                print(output.add_2_num()) # problem solved
                out = output.add_2_num()
                print("Do you want to include another number? Y/N")
                answer = input(":")
                if answer == 'Y' or 'y' or 'Yes' or 'yes':
                    print("Type in a number")
                    answer1 = int(input(":"))
                    a = (number(out,answer1))
                    p = int(input(("If you want to add, press '1'\nIf you want to subract, press '2'\nIf you want to multiply, press '3'\nIf you want to divide, press '4'\n:")))
                    if p == 1:
                        print(a.add_2_num())
                        break
                    elif p == 2:
                        print(a.subtract_2_num())                 
                        break
                    elif p == 3:
                        print(a.multiply_2_num()) 
                        break
                    elif p == 4:
                        print(a.divide_2_num())
                        break
                    else:
                        "This value cannot be accpeted!"
                elif answer == 'N' or 'n' or 'No' or 'no':
                    break
            elif s == '2':
                print(output.subtract_2_num())
                out = output.subtract_2_num()
                print("Do you want to include another number? Y/N")
                answer = input(":")
                if answer == 'Y' or 'y' or 'Yes' or 'yes':
                    print("Type in a number")
                    answer1 = int(input(":"))
                    p = int(input("If you want to add, press '1'\nIf you want to subract, press '2'\nIf you want to multiply, press '3'\nIf you want to divide, press '4'\n:"))
                    a = number(out, answer1)
                    if p == 1:
                        print(a.add_2_num())
                        break
                    elif p == 2:
                        print(a.subtract_2_num())
                        break
                    elif p == 3:
                        print(a.multiply_2_num())
                        break
                    elif p == 4:
                        print(a.divide_2_num())
                        break
                elif answer == 'N' or 'n' or 'No' or 'no':
                    break

                     
            elif s == '3':
                print(output.multiply_2_num())
                out = output.multiply_2_num()
                print("Do you want to include another number? Y/N")
                answer = input(":")
                if answer == 'Y' or 'y' or ' Yes' or 'yes':
                    print("Type in a number")
                    answer1 = int (input(":"))
                    p = int(input("If you want to add, press '1'\nIf you want to subract, press '2'\nIf you want to multiply, press '3'\nIf you want to divide, press '4'\n:"))
                    a = number(out, answer1)
                    if p == 1:
                        print(a.add_2_num())
                        break
                    elif p == 2: 
                        print(a.subtract_2_num())
                        break
                    elif p == 3:
                        print(a.multiply_2_num())
                        break
                    elif p == 4:
                        print(a.divide_2_num())
                        break
                elif answer == 'N' or 'n' or 'no' or 'No':
                    break
                break
            elif s == '4':
                print(output.divide_2_num())
                out = output.divide_2_num()
                print("Do you want to include another number? Y/N")
                answer = input(":")
                if answer == 'Y' or 'y' or 'Yes' or 'yes':
                    print("Type in a number")
                    answer1 = int(input(":"))
                    p = int(input("If you want to add, press '1'\nIf you want to subract, press '2'\nIf you want to multiply, press '3'\nIf you want to divide, press '4'\n:"))
                    a = number(out, answer1)
                    if p == 1:
                        print(a.add_2_num())
                        break
                    elif p == 2:
                        print(a.subtract_2_num())
                        break
                    elif p == 3:
                        print(a.multiply_2_num())
                        break
                    elif p == 4:
                        print(a.divide_2_num())
                        break
                elif answer == 'N' or 'n' or 'no' or 'No':
                    break
            else:
                print("""
                -----------------------------------------------
                This value cannot be accepted. Please try agian
                -----------------------------------------------""")
                continue
                
except:
    print("This value cannot be accepted")
