def whisper_cipher(text: str, shift: int) -> str:
	result = ""

	for char in text:
		if char.isalpha():
			if char.islower():
				base = ord('a')
			else:
				base = ord('A')
			result += chr((ord(char) - base + shift) % 26 + base)
		else:
			result += char

	return result

if __name__ == "__main__":
	print(whisper_cipher("hello", 3))
	print(whisper_cipher("Hello World!", 1))
	print(whisper_cipher("xyz", 3))
	print(whisper_cipher("ABC123def", 5))
	print(whisper_cipher("", 10))
