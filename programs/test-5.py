# Rey | Tugas 9

def reverse(str):
    temp = ""

    for i in range(len(str)):
        temp += str[len(str) - i - 1]


    return temp


def isPalindrom(a, b):
    if a == b:
        return "Kalimat termasuk palindrom"
    else:
        return "Kalimat bukan termasuk palindrom"


def main():
    a = input("Masukkan kalimat: ")
    
    b = reverse(a)
    print("Hasil: {} | {}".format(b, isPalindrom(a, b)))


main()