def garden_operations():
    try:
        print("Testing ValueError...")
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    try:
        print("Testing ZeroDivisionError...")
        x = 10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    try:
        print("Testing FileNotFoundError...")
        open("missing.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    try:
        print("Testing KeyError...")
        plants = {"tomato": 10, "carrot": 5}
        print(plants["missing_plant"])
    except KeyError:
        print("Caught KeyError: 'missing_plant'\n")


def test_error_types():
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    try:
        print("Testing multiple errors together...")
        x = int("abc") / 0
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
