def prime(num):
    is_prime= True
    for i in range(2,num- 1):
        print(i)
        if num % i==0:
           is_prime=False
    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")

prime_num=int(input("input your number: "))

prime(prime_num)