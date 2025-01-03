class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def divide(a, b):
    if b == 0:
        raise CustomError("Division by zero is not allowed.")
    return a / b

try:
    p = int(input("Enter a Number1: "))
    q = int(input("Enter a Number2: "))

    result = divide(p, q)
    print(f"Division is: {result}")
    
except CustomError as e:
    		print(f"CustomError: {e}")