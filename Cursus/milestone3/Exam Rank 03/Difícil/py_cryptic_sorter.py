def count_vowels(strings):
    vowels= "aeiou"
    count = 0

    for char in strings.lower():
          if char in vowels:
                count += 1

    return count

def sort_key(strings):
	return (len(strings), strings.lower(), count_vowels(strings))

def cryptic_sorter(strings: list[str]) -> list[str]:
    if not strings:
        return []

    return sorted(strings, key=sort_key)


if __name__ == "__main__":
    print(cryptic_sorter(["apple", "cat", "banana", "dog", "elephant"]))
    print(cryptic_sorter(["aaa", "bbb", "AAA", "BBB"]))
    print(cryptic_sorter(["hello", "world", "hi", "test"]))
    print(cryptic_sorter([]))
    print(cryptic_sorter([""]))
