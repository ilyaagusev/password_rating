def main():
    user_text = input('Введите пароль: ')
    password_length = len(user_text)

    if password_length <= 12:
        password_length = 'Короткий пароль'
    else:
        password_length = 'Длинный пароль'

    found_digit = any(letter.isdigit() for letter in user_text)
    if found_digit:
        found_digit = 'Содержит цифры'
    else:
        found_digit = 'Не содержит цифры'
    return '{0}\n{1}'.format(password_length, found_digit)


if __name__ == "__main__":
    print(main())
