fizzbuzz=0
for circle in range(1,101):
    fizzbuzz=circle
    if circle % 3 == 0 and circle % 5 ==0:
        fizzbuzz="fizzbuzz"
    elif circle % 3 == 0:
        fizzbuzz="fizz"
    elif circle % 5 == 0:
        fizzbuzz="buzz"
    print(fizzbuzz)
