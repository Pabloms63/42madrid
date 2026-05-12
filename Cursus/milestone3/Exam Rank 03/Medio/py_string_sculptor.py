def string_sculptor(text: str) -> str:
    result = ""
    lower = True

    for char in text:
        if char.isalpha():
            if lower:
                result += char.lower()
            else:
                result += char.upper()
            lower = not lower
        else:
            result += char

    return result


if __name__ == "__main__":
	print(string_sculptor("HOLA"))
