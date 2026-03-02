import pandas as pd

nato_data = pd.read_csv("nato_phonetic_alphabet.csv")


nato_dict = nato_data.to_dict()


letter_list = [nato_dict["letter"][i] for i in range(len(nato_dict["letter"]))]
letters = {"letter":letter_list}
code_list = [nato_dict["code"][i] for i in range(len(nato_dict["letter"]))]
codes = {"code":code_list}

let_code = {letters["letter"][i]:codes["code"][i] for i in range(len(letter_list))}
word_input = str(input("Enter a word: "))

final_code = []
for i in range(len(word_input)):
    for k in let_code:
        if word_input[i] == let_code[k][0]:
            final_code.append(let_code[k])

statement = " ".join(final_code)

print(statement)