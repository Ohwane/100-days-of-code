import math

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operation = {
            "+":add,
            "-":subtract,
            "*":multiply,
            "/":divide
            }
def calculator():

    num1=int(input("What's the first number: "))
    num2=int(input("What's the second number: "))
    print("\nlist of operators:")

    for symbol in operation:
        print(symbol)

    op=input("What's the operation: ")

    calculation_function=operation[op]
    answer=calculation_function(num1,num2)
    print(answer)

    repeat=True

    while repeat:
            option=input(f"would you like to continue? y/n: ").lower()

            if option== "y":
                num3=int(input("What's the number: "))
                print("\nlist of operators:")

                for symbol in operation:
                    print(symbol)

                op=input("What's the operation: ")
                print(f"{answer} {op} {num3}")

                calculation_function=operation[op]
                answer=calculation_function(answer,num3)

                print(answer)

            elif option=="n":
                repeat=False
            else:
                print(f"This isnt a valid input, try again.\n")
                repeat=True
    redo=input(f"would you like to start afresh? (y/n): ").lower()
    if redo=="y": 
        calculator()
    elif redo=="n":
         print("Bye")
calculator()

