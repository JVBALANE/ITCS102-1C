def GreetWithName(name):
    print(f"Hi {name} hope you'll have a wonderful day")

def GreetPerson(name, loc, age):
    print(f"Hi {name} from {loc}, {age} yr\'s old")

def FunctionWithReturn(number):
    print(f"The summation of all numbers from 1 to {number}")
    sum = 0
    for x in range(1, number + 1, 1):
        sum += x
    return sum


def Factorial(number):
    print(f"The factorial of all numbers from 1 to {number}")
    factorial = 1
    for x in range(1, number + 1, 1):
        factorial *= x
    return factorial
