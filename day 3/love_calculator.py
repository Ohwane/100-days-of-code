print("hello! And welcome to the love calculator")
first_name=input("please enter the first name below:\n")
second_name=input("please enter the second name below:\n")

lower_first=first_name.lower()
let1T=lower_first.count("t")
let1R=lower_first.count("r")
let1U=lower_first.count("u")
let1E=lower_first.count("e")

let1L=lower_first.count("l")
let1O=lower_first.count("o")
let1V=lower_first.count("v")
let1e=lower_first.count("e")

lower_second=second_name.lower()
let2T=lower_second.count("t")
let2R=lower_second.count("r")
let2U=lower_second.count("u")
let2E=lower_second.count("e")

let2L=lower_second.count("l")
let2O=lower_second.count("o")
let2V=lower_second.count("v")
let2e=lower_second.count("e")

first_dig=let1T+let2T+let1R+let2R+let1U+let2U+let1E+let2E
second_dig=let1L+let2L+let1O+let2O+let1V+let2V+let1e+let2e
love_score= str(first_dig) + str(second_dig)
print("your love score is: " + love_score + "%")

if int(love_score)<30:
    print("well... y'all could do better")
elif int(love_score)<50:
    print("y'all are doing good")
else:
 print("you make a lovely couple")
