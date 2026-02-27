# import random
#
# names = ["ohwane", "aang", "sokka", "katara", "toph"]
#
# name_dict = {student:score for student in names for score in range(random.randint(30,88))}
#
# passed = {student:score for (student, score) in name_dict.items() if score > 50}
#
# print(passed)

# sentence = "what is the airspeed velocity of an unladen swallow?"
# remove_symbol=sentence.split("?")
# word_list = remove_symbol[0].split(" ")
# print(word_list)
#
# word_count = {word:len(word) for word in word_list}
#
# print(word_count)

weather_c = {"Monday": 12,
             "Tuesday": 14,
             "Wednesday": 15,
             "Thursday": 14,
             "Friday": 21,
             "Saturday": 22,
             "Sunday": 24}

weather_f = {day:temp*9/5+32 for (day, temp) in weather_c.items()}

print(weather_f)