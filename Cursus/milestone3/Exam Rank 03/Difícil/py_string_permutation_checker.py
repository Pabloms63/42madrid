def string_permutation_checker(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    freq1 = {}
    freq2 = {}

    for char in s1:
        if char in freq1:
            freq1[char] += 1
        else:
            freq1[char] = 1

    for char in s2:
        if char in freq2:
            freq2[char] += 1
        else:
            freq2[char] = 1

    return freq1 == freq2


if __name__ == "__main__":
	print(string_permutation_checker("amor", "roma"))
