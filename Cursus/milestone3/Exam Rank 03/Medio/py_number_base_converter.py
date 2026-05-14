def to_base_36(number: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if number == 0:
        return "0"

    result = ""

    while number > 0:
        remainder = number % 36
        result = digits[remainder] + result
        number //= 36

    return result

def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    try:
        number_int = int(number, from_base)

        if to_base == 2:
            return bin(number_int)[2:]
        elif to_base == 10:
            return str(number_int)
        elif to_base == 16:
            return hex(number_int)[2:].upper()
        elif to_base == 36:
            return to_base_36(number_int)
    except ValueError:
        return "ERROR"

if __name__ == "__main__":
    print(number_base_converter("1010", 2, 10))
    print(number_base_converter("FF", 16, 10))
    print(number_base_converter("255", 10, 16))
    print(number_base_converter("123", 10, 2))
    print(number_base_converter("Z", 36, 10))
    print(number_base_converter("35", 10, 36))
    print(number_base_converter("123", 1, 10))
    print(number_base_converter("G", 16, 10))
