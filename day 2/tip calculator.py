print("Welcome to the tip calculator!")
x=int(input("what was the total bill? "))
y=int(input("how many people split the bill? "))
per_tip=int(input("what percentage tip would you like to give? 10, 12 or 15: "))
dec_tip=1
if per_tip == 10:
 dec_tip==0.1*x
 totalpay=x + dec_tip
 finalpay=str(totalpay/y)
 print(x)
 print(y)
 print(per_tip)
 print("each person should pay:"+ finalpay)
elif per_tip==12:
 dec_tip==0.12*x
 totalpay=x + dec_tip
 finalpay=str(totalpay/y)
 print(x)
 print(y)
 print(per_tip)
 print("each person should pay:"+ finalpay)
elif per_tip==15:
 dec_tip==0.15*x
 totalpay=x + dec_tip
 finalpay=str(totalpay/y)
 print(x)
 print(y)
 print(per_tip)
 print("each person should pay:"+ finalpay)
else:
   print("that's not an available tip option")


