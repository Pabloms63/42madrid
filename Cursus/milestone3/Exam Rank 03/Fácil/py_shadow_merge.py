def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
	return sorted(list1 + list2)


if __name__ == "__main__":
	print(shadow_merge([1], [2, 3, 4]))
