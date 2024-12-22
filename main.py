def print_hi():
    heart_rate = 60
    denominator = input('Введите делитель: ')
    try:
        denominator = float(denominator)
        new_heart_rate = heart_rate / denominator
        print(f'Новая ЧСС: {new_heart_rate}')
    except ZeroDivisionError:
        print('Не делите, пожалуйста, на ноль')
    except ValueError:
        print('Используйте только цифры и разделитель "." для ввода')


if __name__ == '__main__':
    data = input()

    list_data = data.split()
    max_len = 0
    result = ""

    for word in list_data:
        if len(word) > max_len:
            max_len = len(word)
            result = word

    print(result)
