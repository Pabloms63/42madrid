def count_vowels(s: str) -> int:
    vowels = "aeiou"
    count = 0

    for char in s.lower():
        if char in vowels:
            count += 1

    return count


def sort_key(s: str):
    return (len(s), s.lower(), count_vowels(s))


def cryptic_sorter(strings: list[str]) -> list[str]:
    if not strings:
        return []

    return sorted(strings, key=sort_key)


if __name__ == "__main__":
	print(cryptic_sorter(["apple", "cat", "banana", "dog", "elephant"]))
