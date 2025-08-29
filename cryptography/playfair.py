import math

def encode(keyword: str, text: str):
    if len(keyword) < 3 or len(keyword) > 8:
        raise RuntimeError("keyword should have a length between 3 and 8")
        
    if not keyword.isalpha():
        raise RuntimeError("keyword cannot contain non-alphabet")
        
    if any(c.isdigit() for c in text):
        raise RuntimeError("Text cannot contain non-alphabet")

    keyword = keyword.upper()
    text = text.upper()

    if 'J' in keyword and 'I' in keyword:
        raise RuntimeError("Cannot have letter I and J in the same keyword")

    for c in keyword[:-1]:
        if c in keyword[keyword.find(c) + 1:]:
            raise RuntimeError(f"Cannot have duplicated letter in keyword: {c}")

    diagram = [c for c in keyword if c != ' ']
    temp_text = [c for c in text if c != ' ']

    for c in range(65, 91):
        if chr(c) in diagram:
            continue

        if chr(c) == 'I' and 'J' in diagram:
            continue

        if chr(c) == 'J' and 'I' in diagram:
            continue

        diagram.append(chr(c))

    i = 0
    while i < len(temp_text):
        if i == len(temp_text) - 1:
            temp_text.append('X')

        if temp_text[i] == temp_text[i + 1]:
            temp_text.insert(i + 1, 'X') 

        # print(temp_text[i:i+2], len(temp_text) - 1, i)

        i += 2

    print("Diagram:")
    i = 1
    while i <= 5:
        print(*diagram[(i-1)*5:(i)*5])

        i += 1

    pos = [[diagram.index(c) % 5, int(diagram.index(c) / 5)] for c in temp_text]

    enc_pos = []

    i = 0
    while i < len(pos) - 1:
        row = abs(pos[i][0] - pos[i + 1][0])
        col = abs(pos[i][1] - pos[i + 1][1])
        enc_pos.append([col, row])

        i += 2

    print(f"\nText: {temp_text}") 
    print(f"Col, Row:{pos}")
    print(f"Enc pos: {enc_pos}")

    i = 0
    while i < len(temp_text):
        if i == len(temp_text) - 1:
            temp_text.append('X')

        if temp_text[i] == temp_text[i + 1]:
            temp_text.insert(i + 1, 'X') 

        # print(temp_text[i:i+2], len(temp_text) - 1, i)

        i += 2

    enc = []
    i = 0
    while i < len(temp_text) - 1:
        a = pos[i]        # Letter 1
        b = pos[i + 1]    # Letter 2

        # Row check
        if a[1] == b[1]:
            a[1] += 1 % 5
            b[1] += 1 % 5
        # Col check
        elif a[0] == b[0]:
            a[0] += 0 % 5
            b[0] += 0 % 5
        # Square check
        elif a != b:
            row = abs(pos[i][0] - pos[i + 1][0])
            col = abs(pos[i][1] - pos[i + 1][1])
            
        pos[i] = a
        pos[i + 1] = b

        i += 2
    
    return "".join(temp_text)
