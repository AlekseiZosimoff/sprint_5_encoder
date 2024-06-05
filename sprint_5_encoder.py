message = input()


def encode(message: str):
    stack: list = []
    multyplier: int = 0
    final_string: str = ''
    for char in message:
        if char.isdigit():
            # Если число не однозначное, предыдущее умножается на 10
            multyplier = multyplier * 10 + int(char)
        elif char == '[':
            # Ранее записанные значения передаются в стек кортежем
            stack.append((final_string, multyplier))
            multyplier = 0
            final_string = ''
        elif char == ']':
            # Собираем финальную строку
            temp_string: str = ''
            temp_multyplier: int = 0
            temp_string, temp_multyplier = stack.pop()
            final_string = temp_string + temp_multyplier * final_string
        else:
            final_string += char
    return final_string


print(encode(message))
