def from_decimal(number: int, base: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if number == 0:
        return "0"

    result = ""

    while number > 0:
        remainder = number % base
        result = digits[remainder] + result
        number //= base

    return result


def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    if from_base < 2 or from_base > 36:
        return "ERROR"

    if to_base < 2 or to_base > 36:
        return "ERROR"

    try:
        number_int = int(number, from_base)
        return from_decimal(number_int, to_base)
    except ValueError:
        return "ERROR"


if __name__ == "__main__":
    print(number_base_converter("1010", 2, 10))   # 10
    print(number_base_converter("FF", 16, 10))    # 255
    print(number_base_converter("255", 10, 16))   # FF
    print(number_base_converter("255", 10, 8))    # 377
    print(number_base_converter("123", 10, 2))    # 1111011
    print(number_base_converter("Z", 36, 10))     # 35
    print(number_base_converter("35", 10, 36))    # Z
    print(number_base_converter("100", 10, 3))    # 10201
    print(number_base_converter("123", 1, 10))    # ERROR
    print(number_base_converter("G", 16, 10))     # ERROR