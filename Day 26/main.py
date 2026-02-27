# numbers = [1,2,3]
#
# new_list = [n+1 for n in numbers]
#
# name = "ohwane"
#
# name_list = [i for i in name]
#
# double = [n*2 for n in range(1,5) ]
# print(name_list)
# print(new_list)
# print(double)

names = ["ohwane", "aang", "sokka", "katara", "toph"]

short_names = [n for n in names if len(n) < 5]
long_names = [n.upper() for n in names if len(n) > 4]
print(short_names)
print(long_names)

numbers = [1,2,3,4,5,6,7,8,9]

squared_numbers = [n**2 for n in numbers]
even_numbers = [n for n in numbers if n%2==0]

import pandas as pd

with open("file1.txt", mode= "r") as file1:
    file_1 = file1.readlines()

    file1_list = [int(i) for i in file_1]

with open("file2.txt", mode= "r") as file2:
    file_2 = file2.readlines()

    file2_list = [int(i) for i in file_2]

compare = [i for i in file1_list for k in file2_list if i == k]
print(compare)
print(squared_numbers)
print(even_numbers)