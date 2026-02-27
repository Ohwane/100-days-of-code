from write_name import names

with open("./input/letter/letter.doc") as letter:
    ltrs = letter.read()

for i in names:
    with open(f"./output/{i}_letter.doc", mode="w") as out_ltrs:

        new_print = ltrs.replace("{name}", i)
        print(new_print)
        out_ltrs.write(new_print)
