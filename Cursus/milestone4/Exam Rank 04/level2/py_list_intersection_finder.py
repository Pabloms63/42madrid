def list_intersection_finder(lists: list[list[int]]) -> list[int]:
	if not lists:
		return []

	conjunto = set(lists[0])

	for list in lists[1:]:
		conjunto = conjunto & set(list)

	if not conjunto:
		return []

	return sorted(conjunto)

def main() -> int:
	print(list_intersection_finder([
        [5, 2, 3, 4],
        [2, 3, 4, 5],
        [3, 4, 5, 6]
    ]))

if __name__ == "__main__":
	main()