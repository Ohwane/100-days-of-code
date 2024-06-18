import math

def paint(height, width, cover):
    area=(height*width)
    print(f"You need {math.ceil(area/cover)} cans")

height_int=int(input(f"Height of the wall: "))
width_int=int(input(f"width of the wall: "))
coverage=int(input(f"what is the coverage per can: "))
paint(width=width_int, height=height_int,cover=coverage)

