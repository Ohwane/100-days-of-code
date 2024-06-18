# this is blackjack game. two random cards to computer and i. i add to it if my card is less than 17
# if i decide to stop the game or if computer decides to stop it then it compares. if less than 21 but greater 
# than the opponent's then it's a win,  if same number then draw. a full deck. 10-13 are all of a value of 10, first is
# 1 or 11
import random
deck=[11,2,3,4,5,6,7,8,9,10,10,10,10]

me=[random.choice(deck), random.choice(deck)]
computer=[random.choice(deck), random.choice(deck)]


def mesum():
    me_counter=0
    for i in me:
        me_counter+=1

    me_sum=0
    for count in range(me_counter):
        me_sum+=me[count]
    return me_sum

def compsum():
    comp_counter=0
    for i in computer:
        comp_counter+=1

    comp_sum=0
    for count in range(comp_counter):
        comp_sum+=computer[count]
    return comp_sum

def deal_card():
    me.append(random.choice(deck))
    
print(
f"""Hello! and welcome to BlackJack
-------------------------------
""")

def result():
    print(f"my cards: {me}, current score {mesum()}" )

    print(f"computer's first card: [{computer[0]}]\n")

def ask_me_deal():
    ask_deal=input("do you want another card (y/n): ")
    if ask_deal=="y":
        deal_card()
        result()
    elif ask_deal=="n":
        result()

def ask_comp_deal():
    comp_choice=["y","n"]
    comp_deal=random.choice(comp_choice)
    if comp_deal=="y":
        computer.append(random.choice(deck))
    elif comp_deal=="n":
        pass
    else:
        print("error")

def ending():
    if mesum() > compsum():
        if mesum()<=21:
            print(f"me: {mesum()}")
            print(f"computer: {compsum()}")
            print("Congratulations! You Win")
        elif mesum()>21:
            if compsum()<=21:
                print(f"me: {mesum()}")
                print(f"computer: {compsum()}")
                print("You Lose")
            else:
                print(f"me: {mesum()}")
                print(f"computer: {compsum()}")
                print("Draw!")
    
    elif compsum() > mesum():
        if compsum()<=21:
            print(f"me: {mesum()}")
            print(f"computer: {compsum()}")
            print("You Lose")
        elif compsum()>21:
            if mesum()<=21:
                print(f"me: {mesum()}")
                print(f"computer: {compsum()}")
                print("Congratulations! You Win")
            else:
                print(f"me: {mesum()}")
                print(f"computer: {compsum()}")
                print("Draw!")

result()

quest=True
while quest:
    if mesum() < 21:
        ask_me_deal()
    else:
        pass
    if compsum() < 21:
        ask_comp_deal()
    else:
        pass
    if mesum() >= 21:
        ending()
        quest=False
    elif compsum() >= 21:
        ending()
        quest=False
    else:
        pass

print(computer)
