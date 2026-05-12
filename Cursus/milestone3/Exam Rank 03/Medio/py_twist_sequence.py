def twist_sequence(arr: list[int], k: int) -> list[int]:
    if k > len(arr):
        k = k % len(arr)

    array2 = arr[-k:]
    array1 = arr[:-k]
    result = array2 + array1

    return result


if __name__ == "__main__":
	print(twist_sequence([1, 2, 3, 4], 0))
