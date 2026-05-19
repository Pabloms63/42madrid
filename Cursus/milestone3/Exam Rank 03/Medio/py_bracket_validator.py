def bracket_validator(s: str) -> bool:
    stack = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs.keys():
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
            
    return len(stack) == 0


if __name__ == "__main__":
    print(bracket_validator("(Hola)"))
    print(bracket_validator("([]{})")) 
    print(bracket_validator("(]"))
    print(bracket_validator("([)]"))
    print(bracket_validator("("))
