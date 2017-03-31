def tear(t):
    for times in range(10):
        c=(255,25,15)
        t.circle(times * 2)
        t.left(10)
        t.forward(10)
        
def L(t,distance,angle):
    t.forward(distance)
    t.left(angle)
    t.forward(distance)
    

def polygon(t,c,sides, distance):
    angle = 360 / sides
    t.color(c)
    t.begin_fill()
    for times in range(sides):
        t.forward(distance)
        t.left(angle)
    t.end_fill()

def cool(t):
    t.color("black")
    polygon(t,7,25)
    t.color("orange")
    polygon(t,6,25)

def coolsquared(t):
    for times in range(4):
        cool(t)
        t.right(90)

def jump(t,x,y):
    t.pu()
    t.goto(x,y)
    t.pd()

def polygon_nc(t,sides,distance):
    angle = 360 / sides
    for times in range(sides):
        t.forward(distance)
        t.left(angle)

def flower(t,size):
    for times in range(10):
        t.left(times*36)
        tears(t,size)
        t.penup()
        t.home()
        t.pendown()

def tears(t,size):
    t.width(1)
    for times in range(10):
        t.begin_fill()
        c=(0,170,255)
        t.color(c)
        t.circle(times*2)
        t.left(10)
        t.forward(size)
        t.end_fill()

def star(t,distance):
    t.begin_fill()
    for times in range(6):
        t.forward(distance)
        t.left(72)
        t.forward(distance)
        t.right(144)

def snakel(t):
    t.width(20)
    t.left(45)
    t.left(90)
    t.forward(200)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(150)
    t.right(90)
    t.forward(150)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.right(90)
    polygon(t,"black",4,50)

def snaker(t):
    t.width(20)
    t.right(180)
    t.right(90)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    polygon(t,"black",4,50)


    

        



    
