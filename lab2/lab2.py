"""
1.	Необходимо реализовать алгоритм RSA.
2.	Два простых числа могут генерироваться как сами, так и введены пользователем.
3.	На вход подается строка из латинских букв разного регистра, цифр, знаков препинания и пробела.
4.	Пользователь на выбор может как зашифровать, так и расшифровать входные данные.
5.	Позволяется использование любого языка программирования.
"""
import random
import sys

_ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" \
            "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" \
            " +-*\\=_:;.,?!\"'`%$&@#<>{}()[]" \
            "0123456789"


def code_int(src: int, ed: int, n: int) -> int:
    """
    C = src^e(mod n)
    """
    return (src ** ed) % n


def is_simple(n: int) -> bool:
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** .5) + 1, 2):
        if n % i == 0:
            return False
    return True


def gen_simple(nt: int = -1) -> int:
    res = random.randint(2 ** 3, 2 ** 10)

    while not is_simple(res) or res == nt:
        res += 1

    return res


def gcd(a: int, b: int):
    while a:
        b, a = a, b % a
    return abs(b)


def get_e(fi: int) -> int:
    res = 2
    while res < fi and (gcd(fi, res) != 1):
        res += 1

    if res >= fi:
        raise RuntimeError("hz")

    return res


def get_d(fi: int, e: int) -> int:
    i = 1
    d = 0.1
    while int(d) != d or d == e:
        d = (1 + fi * i) / e
        i += 1

    return int(d)


def rsa_get_keys(p: int = None, q: int = None) -> tuple[tuple[int, int], tuple[int, int]]:
    if p is None:
        p = gen_simple()
    if q is None:
        q = gen_simple()
    if not is_simple(p):
        raise TypeError("p is not simple")
    if not is_simple(q):
        raise TypeError("q is not simple")
    if p == q:
        raise TypeError("q and p is not different")

    n = p * q
    fi = (p - 1) * (q - 1)
    e = get_e(fi)
    d = get_d(fi, e)
    print(n, fi, e, d, p, q, "--")

    return (e, n), (d, n)


def encode_str(text: str, key: tuple[int, int]) -> str:
    return " ".join((str(code_int(_ALPHABET.index(t), *key)) for t in text))


def decode_str(text: str, key: tuple[int, int]) -> str:
    return "".join((_ALPHABET[code_int(i, *key)] for i in (int(t) for t in text.strip().split())))


if __name__ == '__main__':
    print("="*7, "START", "="*7)
    while True:
        try:
            ind = input("Generate p and q? ")

            if ind and ind in "yesYesYEsYESдаДаДА":
                p, q = None, None
            else:
                p, q = map(int, input("Enter two simple numbers: ").strip().split())
                print(p, q)
            open_key, close_key = rsa_get_keys(p, q)

            print("Open: {}, Close: {}".format(open_key, close_key))

            try:
                while True:
                    text = input("Enter text: ")
                    ind = input("Encrypt it? ")

                    if ind and ind in "yesYesYEsYESдаДаДА":
                        print(encode_str(text, open_key))
                    else:
                        print(decode_str(text, close_key))
            except KeyboardInterrupt:
                pass

        except KeyboardInterrupt:
            print("Bye")
            sys.exit()
        except Exception as e:
            print("ERROR: ", e)
