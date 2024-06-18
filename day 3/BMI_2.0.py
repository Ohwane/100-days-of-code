print("hello! nice to meet you. input your details below to calculate your BMI")
weight=float(input("enter mass: "))
height=float(input("enter your height in meters: "))
bmi=round(weight/height**2)

if bmi < 18.5:
    print(f"you bmi is {bmi}")
    print("oops! you are underweight!")
elif bmi<25:
    print(f"you bmi is {bmi}")
    print("you have a normal weight!")
elif bmi<30:
    print(f"you bmi is {bmi}")
    print("you are overweight!")
elif bmi<35:
    print(f"you bmi is {bmi}")
    print("you are obese!")
else:
    print(f"you bmi is {bmi}")
    print("you are clinically obese!")