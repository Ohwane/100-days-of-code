import math

bidding=[]

def add_bid():
    is_people=True

    while is_people:
        new_bidder={}

        name=input("hello, enter your name: ")
        price=int(input("what is you bid price: "))

        new_bidder[name]= price
        # new_bidder["price"]= price

        bidding.append(new_bidder)

        decision=input("are there any other users around(Y/N): ").lower()
        if decision=="y" or decision=="yes":
            is_people=True
        elif decision=="n" or decision=="no":
            is_people=False
            print("The highest bidder is: \n")

        else:
            print("That isn't a valid option, try again")
            is_people=True
add_bid()
print(bidding)

for bid in bidding:
    