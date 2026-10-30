def array_rotation_detector(arr1: list, arr2: list) -> bool:
	if len(arr1) != len(arr2):
		return False
	if not arr1 and not arr2:
		return True
	arr3 = arr1 + arr1
	for i in range(len(arr1)):
		if arr3[i:i + len(arr2)] == arr2:
			return True
	return False

def main() -> int:
	print(array_rotation_detector([1, 2, 3, 4, 5], [5, 1, 2, 3, 4]))

if __name__ == "__main__":
	main()