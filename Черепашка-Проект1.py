print("Калькулятор v.1.0")
print("Умеет выполнять операции с двумя числами")
ch1 = float(input("Введите первое число: "))
ch2 = float(input("Введите второе число: "))
print("Введите нужное действие:")
print("+ - сложение")
print("- - вычитание")
print("* - умножение")
print("/ - деление")
print("** - возведение первого числа в степень второго числа")
print("// - целочисленное деление")
print("% - нахождение остатка от деления")
action = input("Введите действие: ")

if action == "+":
    print(ch1, '+', ch2, '=', ch1 + ch2)
elif action == "-":
    print(ch1, '-', ch2, '=', ch1 - ch2)
