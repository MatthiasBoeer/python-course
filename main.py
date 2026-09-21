from math import pi
from math import factorial


def task_1():
    r = float(input("Input the radius of the circle : "))
    print("The area of the circle with radius " + str(r) + " is: " + str(pi * r ** 2))

def task_2a():
    integer = int(input("Input the integer : "))
    print("Int: ", integer)

    floating_point = float(input("Input the floating point : "))
    print("Float: ", floating_point)

    string = str(input("Input the string : "))
    print("String: ", string)

    boolean = bool(input("Input the boolean : ").lower().startswith('true'))
    print("Boolean: ", boolean)

def task_2b():
    zahl = 10
    print(type(zahl))

    zahl = 10.5
    print(type(zahl))

    text = "Hello, World!"
    print(type(text))

    wahrheitswert = True
    print(type(wahrheitswert))


def task_3():
    zahl_float = float(10)
    print("zahl_float: ",type(zahl_float), zahl_float)

    zahl_int = int(10.5)
    print("zahl_int: ", type(zahl_int), zahl_int)

    zahl_string = str(10)
    print("zahl_string: ", type(zahl_string),zahl_string)

    zahl_from_string = int("10")
    print("zahl_from_string: ", type(zahl_from_string), zahl_from_string)

    boolean_from_int = bool(10)
    print("boolean_from_int: ", type(boolean_from_int), boolean_from_int)


def task_4a(zahl):
    return factorial(zahl)

def task_4b(zahl):
    if(zahl == 0):
        return 1
    if(zahl == 1):
        return 1
    return task_4b(zahl-1)*zahl

def task_4c(zahl):
    out = 1
    for number in range(1, zahl+1):
        out *= number
    return out

if __name__ == '__main__':
    zahl = int(input("Calculate factorial of: "))
    print(task_4c(zahl))