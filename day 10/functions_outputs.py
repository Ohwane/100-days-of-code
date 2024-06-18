import math

# functions with outputs, title cases
# def format_name(f_name,l_name):
#    if f_name=="" or l_name=="":
#     return f"please give a valid input"
#    formatted_f_name=f_name.title()
#    formatted_l_name=l_name.title()
#    return f"Hello {formatted_f_name.title()} {formatted_l_name.title()}, how are you doing?"

# print(format_name(input("Hey, what is your first name: "),input("Hey, waht is your last name: ")))

# # functions with outputs, length
# name_len=len("ohis")
# print(name_len)

def is_leap(year):
    if year % 4==0:
        if year % 100==0:
            if year% 400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def days_in_month(year,month):
    month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap(year) and month==2:
        return 29
    else:
        return month_days[month-1]
    
year=int(input(f"hello, enter the year: "))
month=int(input(f"enter the month: "))
print(days_in_month(year,month))