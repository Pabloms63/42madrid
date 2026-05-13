def twist_sequence(arr: list[int], k: int) -> list[int]:
    if len(arr) == 0:
        return arr

    k = k % len(arr)

    arr_end = arr[-k:]
    arr_start = arr[:-k]

    return arr_end + arr_start


if __name__ == "__main__":
    print(twist_sequence([1, 2, 3, 4, 5], 2))
    print(twist_sequence([1, 2, 3], 1))
    print(twist_sequence([1, 2, 3, 4], 0))
    print(twist_sequence([1, 2, 3], 5))
    print(twist_sequence([], 3))
