from turtle import Turtle, Screen

timmy= Turtle()
timmy.shape("turtle")
timmy.color("green")
my_screen= Screen()

def Allshapes():
  def triangle():
    timmy.color("green")
    for i in range(3):
      timmy.forward(100)
      timmy.right(120)

  def square():
    timmy.color("red")
    for i in range(4):
      timmy.forward(100)
      timmy.right(90)

  def pentagon():
    timmy.color("blue")
    for i in range(5):
      timmy.forward(100)
      timmy.right(72)

  def hexagon():
    timmy.color("orange")
    for i in range(6):
      timmy.forward(100)
      timmy.right(60)

  def heptagon():
    timmy.color("purple")
    for i in range(7):
      timmy.forward(100)
      timmy.right(51.43)

  def octagon():
    timmy.color("pink")
    for i in range(8):
      timmy.forward(100)
      timmy.right(45)

  def nonagon():
    timmy.color("black")
    for i in range(9):
      timmy.forward(100)
      timmy.right(40)

  def decagon():
    timmy.color("grey")
    for i in range(10):
      timmy.forward(100)
      timmy.right(36)
  triangle()
  square()
  pentagon()
  hexagon()
  heptagon()
  octagon()
  nonagon()
  decagon()
#180 60, 360 90, 540 108, 720 120, 900 128.57, 1080 135, 1260 140, 1440 144
Allshapes()
my_screen.exitonclick()