import string


def encode(message: str):
    stack: list = []
    final_string, multyplier = '', ''
    for char in message:
        if char in set(string.digits):
            # Если число не однозначное, предыдущее умножается на 10
            multyplier += char
        elif char == '[':
            # Ранее записанные значения передаются в стек кортежем
            stack.append((final_string, int(multyplier)))
            multyplier = ''
            final_string = ''
        elif char == ']':
            # Собираем финальную строку
            temp_string, temp_multyplier = stack.pop()
            final_string = temp_string + temp_multyplier * final_string
        else:
            final_string += char
    return final_string


def main():
    message = input()
    print(encode(message))


if __name__ == '__main__':
    main()
