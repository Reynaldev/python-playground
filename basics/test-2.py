def main():
    x = int(input("Input harga belanja: "))

    if x > 1500000:
        x -= (x * 0.10)

    print("Total belanja: ", x)


main()