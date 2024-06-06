message = input()


def encode(message: str = '10[2[ba]]'):
    stack: list = []
    final_string: str = ''
    temp_string: str = ''
    multyplier: str = ''
    for char in message:
        if char.isdigit():
            # Если число не однозначное, предыдущее умножается на 10
            multyplier += char
        elif char == '[':
            # Ранее записанные значения передаются в стек кортежем
            stack.append((final_string, int(multyplier)))
            multyplier = ''
            final_string = ''
        elif char == ']':
            # Собираем финальную строку
            temp_string = ''
            temp_multyplier = 0
            temp_string, temp_multyplier = stack.pop()
            final_string = temp_string + temp_multyplier * final_string
        else:
            final_string += char
    return final_string


def main():
    print(encode())


if __name__ == '__main__':
    main()
