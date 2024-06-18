import random
letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers=["0","1","2","3","4","5","6","7","8","9"]
symbols=["!","@","#","$","%","^","&","*","(",")","_","+","{","}","[","}"]
nr_letters=int(input("Enter the number of Letters you want in the password: "))
nr_numbers=int(input("Enter the number of Numbers you want in the password: "))
nr_symbols=int(input("Enter the number of Symbols you want in the password: "))

password=""
# easy version:
# for char in range(1, nr_letters+1):
#     random_char=random.choice(letters)
#     password+=random_char

# for char in range(1, nr_numbers+1):
#     random_num=random.choice(numbers)
#     password+=random_num

# for char in range(1, nr_symbols+1):
#     random_symb=random.choice(symbols)
#     password+=random_symb


# print(password)

# hard version:

password_list=[]
for char in range(1, nr_letters+1):
    password_list.append(random.choice(letters))
for char in range(1, nr_numbers+1):
    password_list.append(random.choice(numbers))
for char in range(1, nr_symbols+1):
    password_list.append(random.choice(symbols))
print(password_list)
random.shuffle(password_list)
print(password_list)
for char in password_list:
    password+=char
print(password)

# hard version2.0 apparantly, shuffling only works for lists :
# for char in range(1, nr_letters+1):
#     random_char=random.choice(letters)
#     password+=random_char

# for char in range(1, nr_numbers+1):
#     random_num=random.choice(numbers)
#     password+=random_num

# for char in range(1, nr_symbols+1):
#     random_symb=random.choice(symbols)
#     password+=random_symb

# print(password)
# random.shuffle(password)
# print(password)