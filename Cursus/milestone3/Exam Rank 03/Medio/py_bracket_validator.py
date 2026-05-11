def bracket_validator(s: str) -> bool:
    stack = []

    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        if char in "([{":
            stack.append(char)

        elif char in ")]}":
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    
    return len(stack) == 0

if __name__ == "__main__":
    print(bracket_validator("(Hola"))
