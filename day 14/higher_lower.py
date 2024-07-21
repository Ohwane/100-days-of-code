from game_data import data

print(f"""\nHello, and welcome to the higher/lower game 
input the option 'A' or 'B' to select a personality with the highest follower count
-----------------------------------------------------------------------------------""")

begin= True

i=1

while begin:
    a_name=data[i]['name']
    a_description=data[i]['description']
    a_place=data[i]['country']
    a_foll=data[i]['follower_count']

    print(f"A: {a_name}, a {a_description}, from {a_place}\n")

    b_name=data[i+1]['name']
    b_description=data[i+1]['description']
    b_place=data[i+1]['country']
    b_foll=data[i+1]['follower_count']
    print(f"B: {b_name}, a {b_description}, from {b_place}")
    
    answer=input(f"What is your answer: ").upper()

    if answer=="A":
        print(f"you selected option A\n")
        if a_foll>=b_foll:
            i+=1
        else:
            print(f"You got it wrong. Game Over!")
            break
    elif answer=="B":
        print(f"you selected option B\n")
        if b_foll>=a_foll:
            i+=1
        else:
            print(f"You got it wrong. Game Over!")
            break
    else:
        print("Invalid option, try again")            
