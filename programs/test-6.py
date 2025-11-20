# Rey | Tugas 10
import math

def reverse(x):
    r = ""

    for i in range(len(x)):
            r += x[len(x) - i - 1]

    return r


def decimalToBinary(x):
    temp = ""

    while math.floor(abs(x)) > 0:
        t = abs(x) % 2
        temp += str(math.floor(t))
        x /= 2

    while len(temp) < 8:
        temp += "0"

    print(temp)

    if x > 0:
        return reverse(temp)
    else:
        temp = reverse(temp)
        r = ""

        for i in range(len(temp) - 1):
            if i == 0: 
                r += "1"
                continue

            r += "1" if temp[i] == "0" else "0"

        r += "1"

        return r


def main():
    x = int(input("Masukkan bilangan desimal: "))
    print("Hasil: ", decimalToBinary(x))


main()