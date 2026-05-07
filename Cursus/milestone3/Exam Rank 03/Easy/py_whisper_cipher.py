def whisper_cipher(text: str, shift: int) -> str:
	result = ""

	for c in text:
		if c.isalpha():
			base = ord('a') if c.islower() else ord ('A')
			result += chr((ord(c) - base + shift) % 26 + base)
		else:
			result += c
	return result


if __name__ == "__main__":
	print(whisper_cipher("hello", 3))
