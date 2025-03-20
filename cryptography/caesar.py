def encode(text: str):
    encoded_str = "" 

    for char in text:
        dec = ord(char)

        if dec >= 65 and dec <= 90:
            dec = ((dec - 65 + 3) % 26) + 65 
        elif dec >= 97 and dec <= 122:
            dec = ((dec - 97 + 3) % 26) + 97

        encoded_str += chr(dec)

    return encoded_str

def decode(text: str):
    encoded_str = "" 

    for char in text:
        dec = ord(char)

        if dec >= 65 and dec <= 90:
            dec = ((dec - 65 - 3) % 26) + 65 
        elif dec >= 97 and dec <= 122:
            dec = ((dec - 97 - 3) % 26) + 97

        encoded_str += chr(dec)

    return encoded_str
