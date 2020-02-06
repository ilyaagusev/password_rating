def main():
    user_text = input('Введите пароль: ')
    print(score_counter(user_text))


def has_digit(user_text):
    return any(letter.isdigit() for letter in user_text)


def has_letters(user_text):
    return any(letter.isalpha() for letter in user_text)


def is_very_long(user_text):
    minimal_password_length = 12
    return len(user_text) > minimal_password_length


def has_uppercase(user_text):
    return any(letter.isupper() for letter in user_text)


def has_lowercase(user_text):
    return any(letter.islower() for letter in user_text)


def has_symbols(user_text):
    return any(
        not letter.isalpha()
        and not letter.isdigit()
        for letter in user_text
    )


def score_counter(user_text):
    checks = [
        is_very_long,
        has_digit,
        has_letters,
        has_lowercase,
        has_uppercase,
        has_symbols
    ]
    score = 0
    for check in checks:
        if check(user_text):
            score += 2
    return score


if __name__ == "__main__":
    main()
