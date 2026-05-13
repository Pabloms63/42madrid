def whisper_cipher(text: str, shift: int) -> str:
	result = ""

	for word in text:
		if word.isalpha():
			if word.islower():
				base = ord('a')
			else:
				base = ord('A')
			result += chr((ord(word) - base + shift) % 26 + base)
		else:
			result += word
	
	return result


if __name__ == "__main__":
	print(whisper_cipher("abc", 1))
