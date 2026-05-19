def echo_validator(text: str) -> bool:
    new_text = ""

    if text == "":
        return False

    for char in text.lower():
        if char.isalpha():
            new_text += char
    
    return new_text == new_text[::-1]
                

if __name__ == "__main__":
    print(echo_validator("racecar"))
    print(echo_validator("A man a plan a canal Panama"))
    print(echo_validator("race a car"))
    print(echo_validator("Was it a car or a cat I saw"))
    print(echo_validator("hello"))
    print(echo_validator("Madam Im Adam"))
    print(echo_validator(""))
