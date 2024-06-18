# fruits=["strawberry","orange","watermelon","grapes","pineapple"]
# vegetables=["celery","tomatoes","peppers"]
# plant=fruits,vegetables
# print(plant)
row1= ["0","0","0"]
row2= ["0","0","0"]
row3= ["0","0","0"]
map=[row1,row2,row3]
full_map=print(f"    1    2    3\n1 {row1}\n2 {row2}\n3 {row3}")
print(full_map)
print("where would you like the treasure to be stored?")
row=int(input("input the row: "))
column=int(input("input the column: "))
treasure=input("what treasure would you like to store: ")
map[row-1][column-1]=treasure
full_map=print(f"    1    2    3\n1 {row1}\n2 {row2}\n3 {row3}")

