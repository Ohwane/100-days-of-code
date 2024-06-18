# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("Isn't the weather nice today?")

# greet()

# def greet(name, location):
#     print("Hello " + name + "! How do you do?")
#     print("You live at " + location + " right?")

# my_name=input("Hello what is your name: ")
# my_location= input("Where do you live: ")
# greet(my_name, my_location)

def caesar():

    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m",
            "n","o","p","q","r","s","t","u","v","w","x","y","z"," ","!","@","#","$","%","^","&","*","(",")","_","-","+","=",
            "[","]"]

    direction= input("do you want to decode or encode text: ")
    text=input("Enter your text to encode: ")
    shift=int(input("Enter your shift number: "))
    output=[]

    if direction == "encode":
        for letter in text:
            position = alphabet.index(letter)
            encode = position + shift
            if encode > 43:
                encode = position - shift
            else:
                encode = position + shift
                output.append(alphabet[encode])

    elif direction == "decode":
        for letter in text:
            position = alphabet.index(letter)
            decode = position - shift
            if decode < 0:
                decode = position + shift
            else:
                decode = position - shift
                output.append(alphabet[decode])

    print(f"{''.join(output)}")