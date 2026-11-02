def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
	if not lists:
		return []

	list1 = lists[0].copy()

	for sublist in lists[1:]:
		list1 = list1 + sublist

	n = len(list1)
	for i in range(n):
		swapped = False
		for j in range(0, n-i-1):
			if list1[j] > list1[j+1]:
				list1[j], list1[j+1] = list1[j+1], list1[j]
				swapped = True
		if not swapped:
			break

	return list1

def main() -> int:
	print(merge_sorted_lists([[5], [1, 3], [2, 4]]))

if __name__ == "__main__":
	main()