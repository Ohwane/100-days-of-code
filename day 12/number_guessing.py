import random
print("\nHello! And welcome to the number guessing game\nI'm thinking of a number between 1-100")
print("--------------------------------------\n")
level=input("Choose your difficulty level. Type 'easy' or 'hard': ").lower()

answer=random.randint(0,101)
# print(answer)

if level=="easy":
    print("Difficulty level set to 'easy'\n")
    tries=10
elif level=="hard":
    print("Difficulty level set to 'hard'\n")
    tries=5

guess_loop= True

while guess_loop:
    if tries==0:
        print(f"You have {tries} tries left\nGame over!")
        print(f"The correct answer is : {answer}")
        guess_loop= False
    else:
        print(f"you have {tries} tries left")
        guess=int(input("Enter your guess:"))

        if guess!=answer:
            tries-=1
            if guess<answer:
                print("Too low!\n")
            else:
                print("Too high!\n")
        else:
            print("You got it right!")
            guess_loop= False
