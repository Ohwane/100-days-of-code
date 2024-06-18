import random

customers={}

print("Welcome to Ohwane's restraunt\n")

i=int(input("how many customers are there? "))
for j in range(i):
    customers[j]=input("enter customer name: ")
    print(customers)
    j+=1

print("The customer to pay for the meal is: ")
cust_num=random.randint(0,j)
print(customers[cust_num])
# seed=int(input("enter a seed number: "))
# i=int(input("how many customers are there: "))
# random.seed(seed)

# namesCSV=input("give me everybody's names seperated by a comma: ")
# names=namesCSV.split(", ")
# randnum=random.randint(0,i)
# print("the person to pay the meal is: ")
# print(names[randnum])