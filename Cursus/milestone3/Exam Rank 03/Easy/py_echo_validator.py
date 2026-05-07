def echo_validator(text: str) -> bool:
    text_cleaned = []

    for c in text.lower():
        if c.isalpha():
            text_cleaned.append(c)

    text_cleaned = "".join(text_cleaned)

    if not text_cleaned:
        return False
    
    return text_cleaned == text_cleaned[::-1]

if __name__ == "__main__":
	print(echo_validator("A man a plan a canal Panama"))
