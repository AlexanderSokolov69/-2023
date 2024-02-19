import turtle
from random import randint
# Импортируем функции и объекты
from figures import stone  # Объект КАМЕНЬ
from figures import sciss  # Объект НОЖНИЦЫ
from figures import paper  # Объект БУМАГА
from figures import make_field  # Функция "Рисуем игровое поле"
# from figures import rect  # Функция "Рисуем прямоугольник"
from figures import figura  # Функция "Рисуем ОБЪЕКТ"


def result():  # Вывод результатов игры
    if human != 0 and comp != 0:
        tom3.goto(0, -80)
        tom3.color("orange")
        if human == 1 and comp == 2 or human == 2 and comp == 3 or (
                human == 3 and comp == 1):
            out = "ПОБЕДА!!!"
        else:
            out = "НЕ ПОВЕЗЛО..."
        tom3.write(out, move=False, align="left",
                   font=("Arial", 28, "bold"))
    else:
        screen.ontimer(result, t=1200)


def check():
    global comp
    if human != 0:
        comp = randint(1, 3)
        if comp == 1:
            figura(tom2, 'stone', num=1)
        elif comp == 2:
            figura(tom2, 'sciss', num=1)
        elif comp == 3:
            figura(tom2, 'paper', num=1)
    else:
        screen.ontimer(check, t=1000)


def click(x, y):  # Обработка клика мыши
    global human, comp
    # print(f"{x}:{y}")
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


human = 0  # Флаг завершения хода игрока
comp = 0  # Флаг завершения хода компьютера
turtle.register_shape('stone', stone)  # Регистрируем КАМЕНЬ
turtle.register_shape('sciss', sciss)  # Регистрируем НОЖНИЦЫ
turtle.register_shape('paper', paper)  # Регистрируем БУМАГУ
turtle.tracer(0, 0)  # Включение скоростного режима
screen = turtle.Screen()  # Активация экрана
screen.listen()  # Включение прослкшивания событий клавиатуры и мыши
screen.onclick(click, btn=1)  # Вызов функции по щелчку мыши
screen.ontimer(check, t=1000)  # Проверка состояния игры и ход компьютера
screen.ontimer(result, t=1200)  # Проверка состояния игры и вывод результата

# Регистрация "рисовальщиков"
tom1 = turtle.Turtle()  # Для рисования фона
tom2 = turtle.Turtle()  # Для отображения хода
tom2.hideturtle()
tom2.right(90)
tom2.color("green")
tom3 = turtle.Turtle()  # Для вывода результатов

tom1.pu()
tom1.hideturtle()
# Рисуем игровое поле
make_field(tom1)

tom1.hideturtle()
turtle.update()
turtle.done()
