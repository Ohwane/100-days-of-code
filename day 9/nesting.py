# dictionary= {"Bug":"An error in a program that prevents the program from runnning as expected.",
#              "Function":"A piece of code that you can easily call over and over again.",
#              "Loop": "The action of doing something over and over again.",

#              }

# print(dictionary["Loop"])

# dictionary["Wilson"]="The son of a resolute protector"

# print(dictionary)

# for key in dictionary:
#     print(key)
#     print(dictionary)

# nesting dictionaries in a  dictionary
travel_log= {
    "Nigeria":{"cities_visited": ["Lagos","Kano","Ibadan"], "total_visits":10},
    "South Africa": {"cities_visited":["Johannesburg","Capetown"], "total_visits": 8}
}

# nesting dictionaries in a  list 
another_travel_log= [
    {
        "country": "Nigeria", 
     "cities_visited": ["Lagos","Kano","Ibadan"], 
     "total_visits":10
     }
     ,
    { 
        "country": "South Africa", 
        "cities_visited":["Johannesburg","Capetown"], 
        "total_visits": 8
        }
]

# print(another_travel_log)

# another_travel_log.append({"country":"Russia","cities_visited":
#                            ["moscow"],"total_visits": 4})

# print(another_travel_log)

def add_new_country(country_visited, cities_visited,times_visited):
    # another_travel_log.append({"country":country,"cities_visited":
    #          [cities_visited],"total_visits": times_visited})
    # new_country={}
    # new_country["country"]=country_visited
    # new_country["visits"]= times_visited
    # new_country["cities"]= cities_visited
    # print(new_country)

add_new_country("russia", ["moscow"], 5)

# print(another_travel_log)