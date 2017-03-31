from myFunction import *
import turtle
bob=turtle.Turtle()
bob.speed(0)
turtle.bgcolor("white")
turtle.colormode(255)

jump(bob,-200,100)
snakel(bob)
jump(bob,200,100)
snaker(bob)


jump(bob,200,-100)
snaker(bob)

jump(bob,-200,-100)
snaker(bob)

jump(bob,0,0)
flower(bob,25)

