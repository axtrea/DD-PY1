def get_random_password(n) -> str:
    import random
    import string
    s = string.ascii_letters + string.digits
    return "".join((random.sample(s, n)))
    ...  # TODO написать функцию генерации случайных паролей

print(get_random_password(8))
