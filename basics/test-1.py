import math

def formula1(a, b, d):
    x1 = (-b + math.sqrt(abs(d))) / (2*a)
    x2 = (-b - math.sqrt(abs(d))) / (2*a)
    print(x1, " atau ", x2)


def formula2(a, b):
    x = -b / 2*a
    print(x)


def main():
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    d = b**2 - 4 * a * c

    if d > 0: 
        formula1(a, b, d)
    elif d < 0: 
        formula1(a, b, d)
    else : 
        formula2(a, b)


main()