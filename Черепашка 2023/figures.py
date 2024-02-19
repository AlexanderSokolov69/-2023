import turtle


# Камень
stone = ((47, 17), (61, 18), (70, 22), (75, 27),
         (78, 34), (86, 72), (81, 76), (67, 77),
         (34, 77), (22, 74), (14, 70), (14, 50),
         (18, 40), (21, 30), (28, 24), (34, 21))

# Ножницы
sciss = ((21, 17), (50, 42), (65, 12), (58, 49),
         (71, 60), (77, 56), (81, 60), (69, 72),
         (51, 54), (42, 72), (27, 68), (28, 63),
         (33, 65), (41, 52))

# Бумага
paper = ((22, 15), (33, 27), (51, 16), (62, 27),
         (78, 16), (81, 73), (63, 82), (55, 70),
         (35, 81), (21, 70))


def rect(tom: turtle.Turtle, x1, y1, x2, y2, color):
    tom.color(color)
    tom.pu()
    tom.goto(x1, y1)
    tom.begin_fill()
    tom.goto(x2, y1)
    tom.goto(x2, y2)
    tom.goto(x1, y2)
    tom.end_fill()


def make_field(tom1):
    rect(tom1, -300, 200, 300, -200, 'blue')
    rect(tom1, -100, 142, 60, 10, "white")
    rect(tom1, 88, 142, 248, 10, "white")
    rect(tom1, -265, -131, -199, -175, "darkblue")
    rect(tom1, -270, -126, -204, -170, "yellow")
    rect(tom1, -185, -131, -119, -175, "darkblue")
    rect(tom1, -190, -126, -124, -170, "yellow")
    rect(tom1, -107, -131, -39, -175, "darkblue")
    rect(tom1, -112, -126, -44, -170, "yellow")
    tom1.goto(-210, -122)
    tom1.shape('stone')
    tom1.shapesize(0.5)
    tom1.color('gray')
    tom1.left(-90)
    tom1.stamp()
    tom1.goto(-135, -126)
    tom1.shape('sciss')
    tom1.stamp()
    tom1.goto(-55, -126)
    tom1.shape('paper')
    tom1.stamp()

    
def figura(tom: turtle.Turtle, name, num=0):
    # tom.clear()
    # tom.goto(55, 140)
    tom.goto(55 + 185 * num, 140)
    tom.shape(name)
    tom.shapesize(1.5)
    tom.stamp()

