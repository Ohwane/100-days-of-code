names = ["Aang", "Sokka", "Katara", "Bumi", "Toph", "Momo", "Zuko", "Appa", "Iroh", "Azula", "Ozai"]

for i in range(len(names)):
    with open(f"./input/names/{names[i]}.doc", mode="w") as name:
        name.write(f"{names[i]}")