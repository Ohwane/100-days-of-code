import random

seed_num=int(input("hello. please enter your seed number: "))
seed=random.seed(seed_num)
random_side=random.randint(0,1)
if random_side==1:
    print("Heads")
else:
    print("Tails")
print(seed)