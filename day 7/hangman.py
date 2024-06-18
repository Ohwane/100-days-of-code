import random

word_list= ["ardvark","baboon","camel"]

chosen_word= random.choice(word_list)
print(chosen_word)
answer= []
end_of_game= False
lives=len(chosen_word)
for dash in chosen_word:
        answer.append("_")
while not end_of_game:
    guess= input("guess a letter: ").lower()
    if guess in answer:
     print(f"you've already guessed {guess} ")
   
    

    for letter in chosen_word:
        if letter == guess :
            print("Right")
        else:
            print("wrong") 
    
    for position in range(len(chosen_word)):
        letter= chosen_word[position]
        if letter==guess:
            answer[position] = letter
    if guess not in chosen_word:
        print(f"you guessed {guess}, that's not in the word, you lose a life")
        lives-=1
        if lives==0:
            end_of_game=True
            print("you lose")
        
    print(f"{' '.join(answer)}")
    if "_" not in answer:
        end_of_game=True
        print("You win!")