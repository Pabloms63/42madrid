def echo_validator(text: str) -> bool:
    text_trimed = text.lower().replace(" ", "")
    if text_trimed == text_trimed[::-1]:
        return True
    return False   

if __name__ == "__main__":
	print(echo_validator("A man a plan a canal Panama"))
