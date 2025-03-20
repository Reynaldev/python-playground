def encode(text: str):
    diagram = []
    temp_text = [c for c in text]

    i = 0
    while i < len(temp_text):
        if i == len(temp_text) - 1:
            temp_text.append('z')

        if temp_text[i] == temp_text[i + 1]:
            temp_text.insert(i + 1, 'x') 

        # print(temp_text[i:i+2], len(temp_text) - 1, i)

        i += 2

    return temp_text 
