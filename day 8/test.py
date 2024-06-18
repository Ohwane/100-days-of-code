from cipher import caesar

print("Welcome to the Caesar's Cipher")

alive= True

while alive:
 caesar()
 answer= input("Would you like to try again? (Y/N)")
 answer.lower()
 if answer != "y":
  alive=False

 