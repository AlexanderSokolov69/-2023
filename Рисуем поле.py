import turtle
from random import randint
# Импортируем функции и объекты
from figures import stone  # Объект КАМЕНЬ
from figures import sciss  # Объект НОЖНИЦЫ
from figures import paper  # Объект БУМАГА
from figures import make_field  # Функция "Рисуем игровое поле"
from figures import rect  # Функция "Рисуем прямоугольник"
from figures import figura  # Функция "Рисуем ОБЪЕКТ"

def result():
    global comp, human, res, win_h, win_c
    tom3.goto(0, -80)
    tom3.color("orange")
    if human == comp:
        out = "НИЧЬЯ.."
    elif human == 1 and comp == 2 or human == 2 and comp == 3 or (
            human == 3 and comp == 1):
        out = "ПОБЕДА!!!"
        win_h = win_h + 1
    else:
        out = "НЕ ПОВЕЗЛО..."
        win_c = win_c + 1
    out = out + f" {win_h}:{win_c}"
    tom3.write(out, move=False, align="left",
               font=("Arial", 22, "bold"))


def check():
    global comp, human, res, win_h, win_c
    if res == 0:
        if human != 0 and comp != 0:
            result()
            res = 1
        elif human != 0:
            comp = randint(1, 3)
            if comp == 1:
                figura(tom2, 'stone', num=1)
            elif comp == 2:
                figura(tom2, 'sciss', num=1)
            elif comp == 3:
                figura(tom2, 'paper', num=1)
    screen.ontimer(check, t=1000)

        
def click(x, y):
    global comp, human, res, win_h, win_c
    print(f"{x}:{y}")
    if res != 0:
        human = 0
        comp = 0
        res = 0
        make_field(tom1)
    if human != 0:
        return
    if -269 < x < -206 and -169 < y < -128:
        figura(tom2, 'stone')
        human = 1
    elif -189 < x < -128 and -169 < y < -128:
        figura(tom2, 'sciss')
        human = 2
    elif -111 < x < -45 and -169 < y < -128:
        figura(tom2, 'paper')
        human = 3
    
human = 0  # 1, 2, 3
comp = 0  # 1, 2, 3
res = 0
win_h = 0
win_c = 0
turtle.register_shape('stone', stone)
turtle.register_shape('sciss', sciss)
turtle.register_shape('paper', paper)
turtle.tracer(0, 0)
screen = turtle.Screen()
screen.listen()
screen.onclick(click, btn=1)  # Реагируем на клик мыши
screen.ontimer(check, t=1000)  # Вызываем функцию CHECK через 1000мс
# screen.ontimer(result, t=1200)

tom1 = turtle.Turtle()
tom2 = turtle.Turtle()
tom2.hideturtle()
tom2.right(90)
tom2.color("green")
tom3 = turtle.Turtle()

tom1.pu()
tom1.hideturtle()
tom1.left(-90)
make_field(tom1)  # Рисуем игровое поле

turtle.update()
turtle.done()
