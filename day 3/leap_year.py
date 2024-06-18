print("welcome to the leap year verifier!")
input_year=int(input("enter the year: "))

if input_year % 4==0 :
    if input_year % 100!=0:
        print("Yup! this is a leap year")
    elif input_year % 100==0:
        if input_year % 400==0:
            print("this is a leap year")
        else:
            print("this isn't a leap year")
else:
    print("this isn't a leap year")