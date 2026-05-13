def echo_validator(text: str) -> bool:
    text_new = ""

    for word in text.lower():
        if word.isalpha():
            text_new += word

    if not text_new:
        return False
    
    return text_new == text_new[::-1]
            

if __name__ == "__main__":
	print(echo_validator("racecar"))
