import random
import string

def generate_password(length, use_uppercase=False, use_lowercase=False, use_digits=False, use_special_chars=False):
    chars = ""
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation

    if not any([use_uppercase, use_lowercase, use_digits, use_special_chars]):
        print("Потрібно вибрати хоча б один тип символів для генерації пароля.")
        return None

    if length < 1:
        print("Довжина пароля повинна бути більше 0")
        return None

    password = "".join(random.choice(chars) for _ in range(length))
    return password

def get_yes_or_no_input(y):
    while True:
        user_input = input(y).lower()
        if user_input in ['так', 'ні']:
            return user_input
        print("Будь ласка, введіть «Так» або «Ні».")

while True:
    try:
        length = int(input("Введіть бажану довжину пароля: "))
        if length < 1:
            raise ValueError("Довжина пароля повинна бути більше 0")
        break
    except ValueError as x:
        print(x)

while True:
    print("Оберіть типи символів для включення в пароль:")
    use_uppercase = get_yes_or_no_input("Включити великі літери (Так/Ні): ") == 'так'
    use_lowercase = get_yes_or_no_input("Включити малі літери (Так/Ні): ") == 'так'
    use_digits = get_yes_or_no_input("Включити цифри (Так/Ні): ") == 'так'
    use_special_chars = get_yes_or_no_input("Включити спеціальні символи (Так/Ні): ") == 'так'

    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)
    if password:
        print(f"Згенерований пароль: {password}")

    confirm = get_yes_or_no_input("Бажаєте згенерувати ще один пароль? (Так/Ні): ")
    if confirm != 'так':
        break
