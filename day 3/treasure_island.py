print("hello and welcome to the treasure island game\nYou will be asked a series of questions\nChoose correctly!")
direction=input("in what direction would you like to go.\n Left or Right? ")
direction=direction.lower()

if direction=="right":
    print("you fell into an abyss. game over!")
elif direction=="left":
    water=input("You have gotten to the river bank, would you swim or wait? ")
    water=water.lower()
    if water=="swim":
        print("you got attacked my crocociles. game over!")
    elif water=="wait":
        door=input("what color of door would you enter?\nblue, red or yellow: ")
        door=door.lower()
        if door=="blue":
            print("you fell into a blackhole")
        elif door=="red":
            print("you encountered a pack of sabre-toothed tigers")
        elif door=="yellow":
            print("Congratulations! You win!")
else:
    print("answer is not valid. game over!")