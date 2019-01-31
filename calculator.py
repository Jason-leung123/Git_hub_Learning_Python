class calculator():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        output = self.num1 + self.num2
        return output
    def subtract(self):
        output = self.num1 - self.num2
        return output
    def multiply(self):
        output = self.num1 * self.num2
        return output
    def divide(self):
        output = self.num1 / self.num2
        return output
try:
    numbers = calculator(int(input("Type in a number: ")), int(input("Type in another number: ")))
    text = input("To add, type in = +\nTo subract, type in = -\nTo multiply, type in = *\nTo divide, type in = /\n:")
    while True:
        if text == '*':
            print(numbers.multiply())
            break
        else:
            print("This value cannot be accepted")
            break
        if text == '+':
            print(numbers.add())
            break
        else:
            print("This value cannot be accepted")
            break
        if text == '-':
            print(numbers.subtract())
            break
        else:
            print("This value cannot be accepted")
            break
        if text == '/':
            print(numbers.divide())
            break
        else:
            print("This value cannot be accepted")
            break
except:
    print("This value cannot be accepted")

