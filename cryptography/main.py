import caesar 
import playfair

if __name__ == "__main__": 
    encoded = caesar.encode("reykaranganyar")
    decoded = caesar.decode(encoded)

    print(f"{encoded}\n{decoded}")

    # print(playfair.encode("security", "hello world"))
