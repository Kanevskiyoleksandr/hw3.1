print("ВВедите значение А")
a =int(input())
print("Введите значение B")
b = int(input())
print("Введите значение V")
v = int(input())
if a > b:
    print("Свершилось!")
if b > a:
    print("Да ну!")
if a == b:
    print("А если так?")
    a = a + v
    b = b - v
    if a > b:
        print("Свершилось!")
    if b > a:
        print("Да ну!")